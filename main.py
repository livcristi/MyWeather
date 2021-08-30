
from PyQt5.QtWidgets import QApplication
from gui.app_main_window import MyMainWindow
from service.helpers.weather_data_mediator import WeatherDataMediator
from service.weather_service import WeatherService
from weather_data_getter.open_weather_forecast import OpenWeatherForecast
from weather_data_getter.weather_predictor import WeatherPredictor

if __name__ == '__main__':
    # Create the application
    app = QApplication([])

    # Create the objects
    forecaster = OpenWeatherForecast()
    predictor = WeatherPredictor()
    mediator = WeatherDataMediator()
    mediator.add_getter(forecaster)
    mediator.add_getter(predictor)

    weather_service = WeatherService(mediator)
    widget = MyMainWindow(weather_service)
    widget.show()

    # Begin the application main loop
    app.exec()
