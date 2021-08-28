import pandas as pd
import geopy.distance
from datetime import datetime, timedelta
import harperdb


class WeatherPredictor:
    def __init__(self):
        self.__db_connection = None
        self.__dataframe = None
        self.__stations = pd.read_csv('./data/stations_data/stations_data.csv')
        # self.__stations = pd.read_csv('C:\\Users\\tereb\\OneDrive\\Desktop\\MyWeather\\data\\stations_data\\stations_data.csv')
        self.__stations['Point'] = [(x, y) for x, y in zip(self.__stations['Latitude'], self.__stations['Longitude'])]
        self.__current_station = 'CLUJ NAPOCA'

    def update_location(self, country, latitude, longitude):
        """
        Finds the closest station to the given location (which will be used to extract prediction data)
        :param country: Country of the location
        :param latitude: Latitude of the location (float)
        :param longitude: Longitude of the location (float)
        :return: Nothing
        """
        if country != 'RO':
            return None
        closest_station = self.__closest_station((latitude, longitude))
        self.__current_station = closest_station

    def __closest_station(self, point):
        """ Find closest station point to a given point. """
        best_point = None
        best_distance = 10000
        points = self.__stations['Point'].tolist()
        for station_point in points:
            current_distance = self.__compute_distance(point, station_point)
            if current_distance < best_distance:
                best_distance = current_distance
                best_point = station_point
        return self.__stations[self.__stations['Point'] == best_point].Name.values[0]

    def get_prediction(self, day=0):
        if self.__db_connection is None:
            url = 'https://weather-pred-livcristi.harperdbcloud.com'
            # filename = 'C:\\Users\\tereb\\OneDrive\\Desktop\\MyWeather\\data\\api_data\\db_api_key.txt'
            filename = './data/api_data/db_api_key.txt'
            with open(filename, 'r') as api_file:
                api_key_encrypted = api_file.readline().strip()
            api_key = ''.join(list(map(lambda x: chr(ord(x) - 3) if x.isalpha() else x, api_key_encrypted)))
            self.__db_connection = harperdb.HarperDB(
                url=url,
                username='Livcristi',
                password=api_key
            )

        if self.__dataframe is None:
            prediction_date_1 = (datetime.today() + timedelta(days=6)).strftime('%Y-%m-%d')
            prediction_date_2 = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
            sql_input = self.__db_connection.sql(
                'SELECT Date, Temp_min, Temp_avg, Temp_max, Precipitation '
                'FROM weather_schema.predictions '
                'WHERE Name = \'{0}\' AND (Date =\'{1}\' OR Date =\'{2}\')'.format(
                    self.__current_station, prediction_date_1, prediction_date_2))
            self.__dataframe = self.__convert_to_dataframe(sql_input)

        return self.__dataframe[self.__dataframe.index == day]

    def __compute_distance(self, coords1, coords2):
        return geopy.distance.distance(coords1, coords2).km

    def __convert_to_dataframe(self, sql_data):
        df = pd.DataFrame(reversed(sql_data))
        df.columns = ['date', 'temperature_min', 'temperature', 'temperature_max', 'prec_prob']
        df.loc[df['prec_prob'] >= 1, 'prec_prob'] = 1
        # Add description
        df['description'] = 'sunny'
        df.loc[(df['prec_prob'] >= 0.7) & (df['temperature'] <= 0), 'description'] = 'snow'
        df.loc[(df['prec_prob'] >= 0.7) & (df['temperature'] > 0), 'description'] = 'rainy'
        df.loc[(40 <= df['prec_prob']) & (df['prec_prob'] < 0.7), 'description'] = 'clouds'
        df.loc[(20 <= df['prec_prob']) & (df['prec_prob'] < 0.4), 'description'] = 'few clouds'
        # Add remaining empty columns
        df['pressure'] = df['humidity'] = df['wind_speed'] = df['wind_dir'] = None
        return df
