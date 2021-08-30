import datetime

import pandas as pd
import requests
from requests.exceptions import HTTPError

from weather_data_getter.weather_forecaster import WeatherForecaster


class OpenWeatherForecast(WeatherForecaster):
    def __init__(self):
        # Read the encrypted api key from the file, decrypt it and save it
        filename = './data/api_data/open_weather_api_key.txt'
        with open(filename, 'r') as api_file:
            api_key_encrypted = api_file.readline().strip()
        api_key = ''.join(list(map(lambda x: chr(ord(x) - 7) if x.isalpha() else x, api_key_encrypted)))
        self.__api_key = api_key      # Init the api key
        self.__dataframe = None       # Init the weather dataframe
        self.__city_data = None

    def get_daily_forecasts(self):
        """
        Gets daily forecast for the next 5 days and returns it as a dataframe
        :return: Pandas dataframe containing weather forecast data
        """
        today_date = datetime.datetime.today()
        forecast_data = [self.__get_date_data((today_date + datetime.timedelta(days=diff)).strftime('%Y-%m-%d'))
                         for diff in range(6)]
        return pd.concat(forecast_data)

    def get_hourly_forecasts(self):
        """
        Gets hourly weather forecasts as a dataframe
        :return: Pandas dataframe containing hourly weather forecasts
        """
        return self.__dataframe

    def update_location(self, location_data):
        """
        Updates the location of the weather predictor, meaning: It tries to get the data from openWeather for the
        given city of the location
        :param location_data: Dictionary which contains the fields: "country", "name", "latitude", "longitude"
        :return: Nothing
        """
        if location_data['city'] is None:
            raise Exception("City is none")
        self.__request_data(location_data['city'])

    def __request_data(self, city):
        """
        Request data from OpenWeatherMap and updates the internal dataframe
        :param city: City from which the weather data is retrieved
        :return: Nothing
        """
        data_request = None
        try:
            # Request weather forecast JSON from open weather API
            data_request = requests.get('https://api.openweathermap.org/data/2.5/forecast?units=metric&q=' + city +
                                        '&APPID=' + self.__api_key)
            if data_request.json()['cod'] != '200' or data_request is None:
                raise Exception("Internet connection error")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

        # Convert the needed data from JSON to a pandas dataframe
        forecast_data = list()
        for measurement in data_request.json()['list']:
            measurement_data = dict()
            measurement_data['city'] = city
            measurement_data['date'] = measurement['dt_txt']
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
        self.__dataframe['date'] = pd.to_datetime(self.__dataframe['date'])
        self.__city_data = {"city": data_request.json()['city']['name'],
                            "country": data_request.json()['city']['country'],
                            "latitude": data_request.json()['city']['coord']['lat'],
                            "longitude": data_request.json()['city']['coord']['lon']}

    def __get_date_data(self, date):
        """
        Gets the data for a certain date from the dataframe
        :param date: Date (str format, dd-mm-yyyy)
        :return: Dataframe with weather data for the given date
        """
        if self.__dataframe is None:
            # print(self.__dataframe)
            raise Exception("Cannot read the data")
        # Get the rows with the given date
        sub_frame = self.__dataframe[self.__dataframe['date'].dt.date == pd.to_datetime(date).date()]
        if sub_frame.empty:
            return None
        # Get the mean values of the day
        median_series = sub_frame.drop(
            columns=['city', 'date', 'description', 'temperature_max', 'temperature_min']).mean(axis=0)
        # Add the string columns (most frequent values per column)
        median_series['temperature_min'] = sub_frame['temperature_min'].min()
        median_series['temperature_max'] = sub_frame['temperature_max'].max()
        median_series['city'] = sub_frame['city'].mode()[0]
        median_series['date'] = pd.to_datetime(date)
        median_series['description'] = sub_frame['description'].mode()[0]
        # Convert the Series to a Dataframe and return it
        median_frame = median_series.to_frame().T
        return median_frame
