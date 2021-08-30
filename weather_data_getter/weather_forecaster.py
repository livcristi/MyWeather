from abc import ABC, abstractmethod

"""
    Interface for the weather forecasters used in the app
"""


class WeatherForecaster(ABC):

    @abstractmethod
    def get_daily_forecasts(self):
        pass

    @abstractmethod
    def get_hourly_forecasts(self):
        pass

    @abstractmethod
    def update_location(self, location_data):
        pass

