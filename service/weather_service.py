from domain.weather_measurement import WeatherMeasurement
from requests import get

from service.helpers.location_finder import LocationFinder

"""
    Module for the app service
"""


class WeatherService:
    def __init__(self, weather_mediator):
        """
        Initializes the service with its dependencies
        :param weather_forecaster: WeatherForecaster object
        :param weather_predictor: WeatherPredictor object (tba)
        """
        # Initializes the mediator
        self.__weather_mediator = weather_mediator
        self.__location_finder = LocationFinder()
        # Gets the user city
        ip = get('https://api.ipify.org').text
        ip_data_json = get('https://ipinfo.io/' + ip + '/json').json()
        ip_data_json['latitude'], ip_data_json['longitude'] = ip_data_json['loc'].split(',')
        ip_data_json['latitude'] = float(ip_data_json['latitude'])
        ip_data_json['longitude'] = float(ip_data_json['longitude'])
        self.city_name = ip_data_json['city']
        self.__weather_mediator.update_location(ip_data_json)

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
        self.__weather_mediator.update_location(self.__location_finder.locate_city(city_name))

    def get_today_weather(self):
        """
        Returns a WeatherMeasurement object containing the weather data of the current day
        """
        return WeatherMeasurement(self.__weather_mediator.get_today_data())

    def get_next_days_weather(self):
        """
        Gets the weather for the next days
        :return: Returns a list of WeatherMeasurement objects which contains the weather data for the following days,
        beginning with a difference of day_index days
        """
        mediator_data = self.__weather_mediator.get_daily_data()
        days_data = [WeatherMeasurement(mediator_data[day:day+1]) for day in range(3)]
        return days_data

    def get_now_weather(self):
        """
        Returns a WeatherMeasurement object containing the weather data of the current hour
        """
        return WeatherMeasurement(self.__weather_mediator.get_now_data())

    def get_next_hours_weather(self):
        """
        Gets the weather for the next few hours
        :return: Returns a list of WeatherMeasurement objects which contains the weather data for the following hours,
        beginning with a difference of hour_index hours
        """
        mediator_data = self.__weather_mediator.get_hourly_data()
        hours_data = [WeatherMeasurement(mediator_data[hour:hour+1]) for hour in range(3)]
        return hours_data

    def update_indexer(self, indexer_type, amount):
        """
        Updates the day/hour indexer
        :param indexer_type: Type of the indexer ('day' or 'hour')
        :param amount: -1 (backward) or 1 (forward)
        :return: The updated measurements or None, if the amount or indexer type are invalid
        """
        updated_data = self.__weather_mediator.update_indexer(indexer_type, amount)
        if updated_data is None:
            return None
        updated_data_measurement = [WeatherMeasurement(updated_data[diff:diff + 1]) for diff in range(3)]
        return updated_data_measurement

