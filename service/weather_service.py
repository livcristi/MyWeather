from datetime import datetime, timedelta
from domain.weather_measurement import WeatherMeasurement
from requests import get

from service.widget_indexer import WeatherWidgetIndexer

"""
    Module for the app service
"""


class WeatherService:
    def __init__(self, weather_forecaster, weather_predictor=None):
        """
        Initializes the service with its dependencies
        :param weather_forecaster: WeatherForecaster object
        :param weather_predictor: WeatherPredictor object (tba)
        """
        # Get the forecaster
        self.__weather_forecaster = weather_forecaster
        self.__weather_predictor = weather_predictor
        # Initializes the indexes for the auxiliary weather items (todo: move this to another class)
        self.__indexer = WeatherWidgetIndexer()
        # Gets the user city
        ip = get('https://api.ipify.org').text
        ip_data_json = get('https://ipinfo.io/' + ip + '/json').json()
        self.city_name = ip_data_json['city']
        self.update_city(self.city_name)

    def get_city_name(self):
        """
        Gets the current city name which is used by the app
        :return: Name of the city (str)
        """
        return self.city_name

    def update_city(self, city_name):
        """
        Updates the app city
        :param city_name: New city name
        :return: Nothing
        """
        try:
            self.__weather_forecaster.update_city(city_name)
            self.city_name = city_name
        except Exception:
            print('Some error occured')

    def get_today_weather(self):
        """
        Returns a WeatherMeasurement object containing the weather data of the current day
        """
        return WeatherMeasurement(self.__weather_forecaster.get_date_data(datetime.today().strftime('%Y-%m-%d')))

    def get_next_days_weather(self):
        """
        Gets the weather for the next days
        :return: Returns a list of WeatherMeasurement objects which contains the weather data for the following days,
        beginning with a difference of day_index days
        """
        # the list of Measurements taken from the weather forecaster
        days_data = [WeatherMeasurement(
            self.__weather_forecaster.get_date_data(
                (datetime.today() + timedelta(days=(self.__indexer.day_index + difference))).strftime('%Y-%m-%d'))
        ) for difference in range(3)]
        return days_data

    def get_now_weather(self):
        """
        Returns a WeatherMeasurement object containing the weather data of the current hour
        """
        return WeatherMeasurement(self.__weather_forecaster.get_hour_measurement(0))

    def get_next_hours_weather(self):
        """
        Gets the weather for the next few hours
        :return: Returns a list of WeatherMeasurement objects which contains the weather data for the following hours,
        beginning with a difference of hour_index hours
        """
        hours_data = [WeatherMeasurement(self.__weather_forecaster.get_hour_measurement(
            self.__indexer.hour_index + diff)) for diff in range(3)]
        return hours_data

    def update_indexer(self, indexer_type, amount):
        """
        Updates the day/hour indexer
        :param indexer_type: Type of the indexer ('day' or 'hour')
        :param amount: -1 (backward) or 1 (forward)
        :return: The updated measurements or None, if the amount or indexer type are invalid
        """
        if indexer_type == 'day':
            if self.__indexer.update_indexer(indexer_type, amount, self.__weather_forecaster.get_days_of_measurements()):
                return self.get_next_days_weather()
            else:
                return None
        else:
            if self.__indexer.update_indexer(indexer_type, amount, self.__weather_forecaster.get_number_of_measurements()):
                return self.get_next_hours_weather()
            else:
                return None

