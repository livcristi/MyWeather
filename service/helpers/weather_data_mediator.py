from threading import Thread

import pandas as pd

from service.helpers.widget_indexer import WeatherWidgetIndexer


class WeatherDataMediator:
    def __init__(self):
        self.__weather_data_getter = list()
        self.__daily_weather_dataframe = None
        self.__hourly_weather_dataframe = None
        self.__indexer = WeatherWidgetIndexer()

    def add_getter(self, getter):
        """
        Adds a new data getter to the mediator
        :param getter: Child class of WeatherForecaster
        :return: Nothing
        """
        self.__weather_data_getter.append(getter)

    def update_location(self, location_data):
        # Update each getter in parallel
        threads = []
        for getter in self.__weather_data_getter:
            thread = Thread(target=getter.update_location, args=(location_data,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        # Update the dataframes
        daily_data = [getter.get_daily_forecasts() for getter in self.__weather_data_getter]
        hourly_data = [getter.get_hourly_forecasts() for getter in self.__weather_data_getter]
        self.__daily_weather_dataframe = pd.concat(daily_data)
        self.__daily_weather_dataframe['date'] = pd.to_datetime(self.__daily_weather_dataframe['date'])
        self.__daily_weather_dataframe.sort_values('date', inplace=True)
        self.__daily_weather_dataframe.reset_index(drop=True, inplace=True)

        self.__hourly_weather_dataframe = pd.concat(hourly_data).sort_values('date')
        self.__hourly_weather_dataframe['date'] = pd.to_datetime(self.__hourly_weather_dataframe['date'])
        self.__hourly_weather_dataframe.sort_values('date', inplace=True)
        self.__hourly_weather_dataframe.reset_index(drop=True, inplace=True)

        self.__indexer.reset_indexer()

    def get_now_data(self):
        if self.__hourly_weather_dataframe is None:
            raise Exception("Cannot get hourly weather data")
        return self.__hourly_weather_dataframe[0:1]

    def get_today_data(self):
        if self.__daily_weather_dataframe is None:
            raise Exception("Cannot get daily weather data")
        return self.__daily_weather_dataframe[0:1]

    def get_hourly_data(self):
        if self.__hourly_weather_dataframe is None:
            raise Exception("Cannot get hourly weather data")
        return self.__hourly_weather_dataframe[self.__indexer.hour_index:(self.__indexer.hour_index + 3)]

    def get_daily_data(self):
        if self.__daily_weather_dataframe is None:
            raise Exception("Cannot get hourly weather data")
        return self.__daily_weather_dataframe[self.__indexer.day_index:(self.__indexer.day_index + 3)]

    def update_indexer(self, indexer_type, amount):
        """
        Updates the day/hour indexer
        :param indexer_type: Type of the indexer ('day' or 'hour')
        :param amount: -1 (backward) or 1 (forward)
        :return: The updated measurements or None, if the amount or indexer type are invalid
        """
        if indexer_type == 'day':
            if self.__indexer.update_indexer(indexer_type, amount, self.__daily_weather_dataframe.shape[0]):
                return self.get_daily_data()
            else:
                return None
        else:
            if self.__indexer.update_indexer(indexer_type, amount, self.__hourly_weather_dataframe.shape[0]):
                return self.get_hourly_data()
            else:
                return None
