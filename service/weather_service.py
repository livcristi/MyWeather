from datetime import datetime, timedelta
from domain.weather_measurement import WeatherMeasurement
from requests import get

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
        self.__day_index = 1
        self.__hour_index = 1
        # Gets the user city
        ip = get('https://api.ipify.org').text
        ip_data_json = get('https://ipinfo.io/' + ip + '/json').json()
        self.city_name = ip_data_json['city']
        self.update_city(self.city_name)

    def get_city_name(self):
        return self.city_name

    def update_city(self, city_name):
        try:
            self.__weather_forecaster.update_city(city_name)
            self.city_name = city_name
        except Exception:
            print('Some error occured')

    def get_today_weather(self):
        return WeatherMeasurement(self.__weather_forecaster.get_date_data(datetime.today().strftime('%Y-%m-%d')))

    def get_next_days_weather(self):
        # Return list of Measurements
        days_data = list()
        for difference in range(3):
            days_data.append(WeatherMeasurement(self.__weather_forecaster.get_date_data(
                (datetime.today() + timedelta(days=(self.__day_index + difference))).strftime('%Y-%m-%d'))
            ))
        return days_data

    def get_now_weather(self):
        return WeatherMeasurement(self.__weather_forecaster.get_hour_measurement(0))

    def get_next_hours_weather(self):
        hours_data = [WeatherMeasurement(self.__weather_forecaster.get_hour_measurement(self.__hour_index + diff))
                      for diff in range(3)]
        return hours_data

    def forward_day(self):
        if self.__day_index + 3 >= self.__weather_forecaster.get_days_of_measurements():
            return None
        else:
            self.__day_index += 1
            # Return list of days
            return self.get_next_days_weather()

    def backward_day(self):
        if self.__day_index == 1:
            return None
        else:
            self.__day_index -= 1
            return self.get_next_days_weather()

    def forward_hour(self):
        if self.__hour_index + 3 >= self.__weather_forecaster.get_number_of_measurements():
            return None
        else:
            self.__hour_index += 1
            return self.get_next_hours_weather()

    def backward_hour(self):
        if self.__hour_index == 1:
            return None
        else:
            self.__hour_index -= 1
            return self.get_next_hours_weather()

