import pandas as pd

"""
    Module for the domain. It contains the class definition for WeatherMeasurement. It is used to encapsulate a pandas 
    dataframe row and get its data.
"""


class WeatherMeasurement:
    def __init__(self, dataframe_row):
        self.row_data = dataframe_row

    @property
    def temperature(self):
        return self.row_data['temperature'].values[0]

    @property
    def temperature_min(self):
        return self.row_data['temperature_min'].values[0]

    @property
    def temperature_max(self):
        return self.row_data['temperature_max'].values[0]

    @property
    def precipitation_chance(self):
        return self.row_data['prec_prob'].values[0]

    @property
    def day(self):
        return pd.to_datetime(str(self.row_data['date'].values[0])).strftime('%d-%m-%Y')

    @property
    def time(self):
        return pd.to_datetime(str(self.row_data['date'].values[0])).strftime("%H:%M")

    @property
    def description(self):
        return self.row_data['description'].values[0]

    @property
    def pressure(self):
        return self.row_data['pressure'].values[0]

    @property
    def humidity(self):
        return self.row_data['humidity'].values[0]

    @property
    def wind_speed(self):
        return self.row_data['wind_speed'].values[0]

    @property
    def wind_dir(self):
        return self.row_data['wind_dir'].values[0]
