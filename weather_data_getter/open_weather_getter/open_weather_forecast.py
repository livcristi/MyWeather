from pprint import pprint

import pandas as pd
import requests
from requests.exceptions import HTTPError


class OpenWeatherForecast:
    def __init__(self, city='London'):
        # Read the encrypted api key from the file, decrypt it and save it
        filename = './data/api_data/api_key.txt'
        with open(filename, 'r') as api_file:
            api_key_encrypted = api_file.readline().strip()
        api_key = ''.join(list(map(lambda x: chr(ord(x) - 7) if x.isalpha() else x, api_key_encrypted)))
        self.__api_key = api_key      # Init the api key
        self.__dataframe = None       # Init the weather dataframe
        self.__request_data(city)

    def __request_data(self, city='London'):
        """
        Request data from OpenWeatherMap and updates the internal dataframe
        :param city: City from which the weather data is retrieved
        :return: Nothing
        """

        data_request = None

        try:
            # Request weather forecast JSON from open weather API
            data_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?units=metric&q=' + city +
                                        '&APPID=' + self.__api_key)
            if data_request.json()['cod'] != '200' or data_request is None:
                raise Exception("Internet connection error")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

        # Convert the needed data from JSON into a pandas dataframe
        forecast_data = list()
        for measurement in data_request.json()['list']:
            measurement_data = dict()
            measurement_data['city'] = city
            measurement_data['dt'] = measurement['dt_txt']
            measurement_data['temperature'] = measurement['main']['temp']
            measurement_data['temperature_min'] = measurement['main']['temp_min']
            measurement_data['temperature_max'] = measurement['main']['temp_max']
            measurement_data['prec_prob'] = measurement['pop']
            measurement_data['pressure'] = measurement['main']['pressure']
            measurement_data['humidity'] = measurement['main']['humidity']
            measurement_data['wind_speed'] = measurement['wind']['speed']
            measurement_data['wind_dir'] = measurement['wind']['deg']
            measurement_data['description'] = measurement['weather'][0]['description']
            forecast_data.append(measurement_data)

        self.__dataframe = pd.DataFrame(forecast_data)
        self.__dataframe['dt'] = pd.to_datetime(self.__dataframe['dt'])

    def update_city(self, city):
        """
        Updates the dataframe with weather data of the new given city
        :param city: City name (str)
        :return: Nothing
        """
        if city is None:
            raise Exception("City is none")
        self.__request_data(city)

    def get_date_data(self, date):
        """
        Gets the data for a certain date from the dataframe
        :param date: Date (str format, dd-mm-yyyy)
        :return: Dataframe with weather data for the given date
        """
        # Get the rows with the given date
        sub_frame = self.__dataframe[self.__dataframe['dt'].dt.date == pd.to_datetime(date).date()]
        if sub_frame.empty:
            return None
        # Get the mean values of the day
        median_series = sub_frame.drop(
            columns=['city', 'dt', 'description', 'temperature_max', 'temperature_min']).mean(axis=0)
        # Add the string columns (most frequent values per column)
        median_series['temperature_min'] = sub_frame['temperature_min'].min()
        median_series['temperature_max'] = sub_frame['temperature_max'].max()
        median_series['city'] = sub_frame['city'].mode()[0]
        median_series['date'] = pd.to_datetime(date)
        median_series['description'] = sub_frame['description'].mode()[0]
        # Convert the Series to a Dataframe and return it
        median_frame = median_series.to_frame().T
        return median_frame

    def get_hour_measurement(self, index):
        """
        Gets the weather data for the given index in the dataframe (hourly measurement)
        :param index: Index in the dataframe (int)
        :return: Dataframe row with the given index
        """
        row_data = self.__dataframe.iloc[index].copy()
        row_data_frame = row_data.to_frame().T
        row_data_frame['date'] = pd.to_datetime(row_data_frame['dt'])
        return row_data_frame

    def get_number_of_measurements(self):
        """
        :return: Returns how many measurements are in the dataframe
        """
        return self.__dataframe.shape[0]

    def get_days_of_measurements(self):
        """
        :return: Returns how many different days are measured in the dataframe
        """
        return len(pd.unique(self.__dataframe['dt'].dt.date))
