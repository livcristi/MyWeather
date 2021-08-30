import pandas as pd
import geopy.distance
from datetime import datetime, timedelta
import harperdb

from weather_data_getter.weather_forecaster import WeatherForecaster

""" Module for the forecaster class which reads data from the database """


class WeatherPredictor(WeatherForecaster):
    def __init__(self):
        self.__db_connection = None
        self.__dataframe = None
        self.__stations = pd.read_csv('./data/stations_data/stations_data.csv')
        self.__stations['Point'] = [(x, y) for x, y in zip(self.__stations['Latitude'], self.__stations['Longitude'])]
        self.__current_station = None

    def update_location(self, location_data):
        """
        Updates the location of the weather predictor, meaning: it finds the closest station to the given location
        (which will be used to extract prediction data)
        :param location_data: Dictionary which contains the fields: "country", "name", "latitude", "longitude"
        :return: Nothing
        """
        # The user attempts to update the location to an invalid one
        if location_data['country'] is None:
            # The choice is to keep the data as it is
            pass

        # The user attempts to update the location to a valid unsupported location
        elif location_data['country'] not in ['RO', 'Ro', 'Romania']:
            # Delete the extracted data and do not return anything
            self.__dataframe = self.__current_station = None

        # The user attempts to update with a valid supported location
        else:
            # Find the closest station to the given location and update the attributes
            closest_station = self.__closest_station((location_data['latitude'], location_data['longitude']))
            self.__current_station = closest_station
            self.__get_database_data()

    def get_daily_forecasts(self):
        """
        Gets the weather forecast for two days in the future (days 6-7 from the current date)
        :return: Pandas dataframe object which holds the forecast data
        """
        # self.__get_database_data()
        return self.__dataframe

    def get_hourly_forecasts(self):
        # Currently there is no data for this method
        return None

    def __closest_station(self, point):
        """
        Find closest station point to a given point.
        :param point: Global coordinate point
        :return: The station name which is the closest to the given point
        """
        best_point = None
        best_distance = 10000
        points = self.__stations['Point'].tolist()
        for station_point in points:
            current_distance = self.__compute_distance(point, station_point)
            if current_distance < best_distance:
                best_distance = current_distance
                best_point = station_point
        return self.__stations[self.__stations['Point'] == best_point].Name.values[0]

    @staticmethod
    def __compute_distance(coords1, coords2):
        """
        Computes the Earth distance (in km) between two tuples of lat-long coordinates
        """
        return geopy.distance.distance(coords1, coords2).km

    @staticmethod
    def __convert_to_dataframe(sql_data):
        """
        Converts the given SQL query data to a dataframe and returns it
        :param sql_data: List of dictionaries
        :return: Pandas dataframe containing forecast data
        """
        # Create a dataframe from the data
        df = pd.DataFrame(reversed(sql_data))
        df.columns = ['date', 'temperature_min', 'temperature', 'temperature_max', 'prec_prob']
        # Sets the precipitation probability
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

    def __get_database_data(self):
        """
        Extracts data from the database and stores it in the dataframe attribute
        :return: Nothing
        """
        # Set up the connection if it does not exist
        if self.__db_connection is None:
            url = 'https://weather-pred-livcristi.harperdbcloud.com'
            # Read the encrypted password key (Caesar cypher much wow), decrypt it and use it for the connection
            filename = './data/api_data/db_api_key.txt'
            with open(filename, 'r') as api_file:
                api_key_encrypted = api_file.readline().strip()
            api_key = ''.join(list(map(lambda x: chr(ord(x) - 3) if x.isalpha() else x, api_key_encrypted)))

            self.__db_connection = harperdb.HarperDB(
                url=url,
                username='Livcristi',
                password=api_key
            )

        # Get the data only if the chosen station is valid
        if self.__current_station is not None:
            # Get the dates for the forecast
            prediction_date_1 = (datetime.today() + timedelta(days=6)).strftime('%Y-%m-%d')
            prediction_date_2 = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
            # SQL query for the data
            sql_output = self.__db_connection.sql(
                'SELECT Date, Temp_min, Temp_avg, Temp_max, Precipitation '
                'FROM weather_schema.predictions '
                'WHERE Name = \'{0}\' AND (Date =\'{1}\' OR Date =\'{2}\')'.format(
                    self.__current_station, prediction_date_1, prediction_date_2))
            # Update the dataframe attribute
            self.__dataframe = self.__convert_to_dataframe(sql_output)
