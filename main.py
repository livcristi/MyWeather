
from PyQt5.QtWidgets import QApplication
from gui.app_main_window import MyMainWindow
from service.weather_service import WeatherService
from weather_data_getter.open_weather_getter.open_weather_forecast import OpenWeatherForecast


if __name__ == '__main__':
    # Create the application
    app = QApplication([])

    # Create the objects
    forecaster = OpenWeatherForecast()
    weather_service = WeatherService(forecaster)
    widget = MyMainWindow(weather_service)
    widget.show()

    # Begin the application main loop
    app.exec()
