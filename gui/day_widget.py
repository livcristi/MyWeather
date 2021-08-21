import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame

"""
    Module for the weather widget in GUI. This widget will display the data related to a measurement (icon for 
    the weather state, temperature, rainfall, wind, etc.). It is used in the main window
"""


class Ui_Form(object):
    def setupUi(self, Form):
        """
        Initialized the widget design (This was automatically generated using the pyuic5 library)
        :param Form: QT Designer Form object
        :return: Nothing
        """
        Form.setObjectName("Form")
        Form.resize(305, 422)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateLabel = QtWidgets.QLabel(Form)
        self.dateLabel.setStyleSheet("font: 12pt \"Franklin Gothic Medium\";\n"
                                     "color: black;")
        self.dateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout.addWidget(self.dateLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.imageWidget = AspectRatioPixmapLabel(Form)
        self.imageWidget.setObjectName("imageWidget")
        self.imageWidget.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout.addWidget(self.imageWidget)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.temperatureLabel = QtWidgets.QLabel(Form)
        self.temperatureLabel.setStyleSheet("font: 10pt \"Franklin Gothic Medium\";\n"
                                            "color: black;")
        self.temperatureLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.verticalLayout.addWidget(self.temperatureLabel)
        self.precipitationLabel = QtWidgets.QLabel(Form)
        self.precipitationLabel.setStyleSheet("font: 10pt \"Franklin Gothic Medium\";\n"
                                              "color: black;")
        self.precipitationLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.precipitationLabel.setObjectName("precipitationLabel")
        self.verticalLayout.addWidget(self.precipitationLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.windSpeedLabel = QtWidgets.QLabel(Form)
        self.windSpeedLabel.setStyleSheet("font: 9pt \"Franklin Gothic Medium\";\n"
                                          "color: black;")
        self.windSpeedLabel.setObjectName("windSpeedLabel")
        self.horizontalLayout_5.addWidget(self.windSpeedLabel)
        self.windDirectionLabel = QtWidgets.QLabel(Form)
        self.windDirectionLabel.setStyleSheet("font: 9pt \"Franklin Gothic Medium\";\n"
                                              "color: black;")
        self.windDirectionLabel.setObjectName("windDirectionLabel")
        self.horizontalLayout_5.addWidget(self.windDirectionLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pressureLabel = QtWidgets.QLabel(Form)
        self.pressureLabel.setStyleSheet("font: 9pt \"Franklin Gothic Medium\";\n"
                                         "color: black;")
        self.pressureLabel.setObjectName("pressureLabel")
        self.horizontalLayout_2.addWidget(self.pressureLabel)
        self.humidityLabel = QtWidgets.QLabel(Form)
        self.humidityLabel.setStyleSheet("font: 9pt \"Franklin Gothic Medium\";\n"
                                         "color: black;")
        self.humidityLabel.setObjectName("humidityLabel")
        self.horizontalLayout_2.addWidget(self.humidityLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dateLabel.setText(_translate("Form", "Date and time"))
        self.temperatureLabel.setText(_translate("Form", "Temperature"))
        self.precipitationLabel.setText(_translate("Form", "Precipitation chance"))
        self.windSpeedLabel.setText(_translate("Form", "Wind speed: "))
        self.windDirectionLabel.setText(_translate("Form", "Wind direction: "))
        self.pressureLabel.setText(_translate("Form", "Pressure: "))
        self.humidityLabel.setText(_translate("Form", "Humidity: "))


class AspectRatioPixmapLabel(QtWidgets.QLabel):
    """
        A custom subclass of QLabel, which is mainly used to hold an icon while keeping its aspect ratio
        The methods here are just the reimplementation of the parent class, with the purpose of keeping the image.
    """

    def __init__(self, parent=None):
        super(AspectRatioPixmapLabel, self).__init__(parent)
        self.pix = QPixmap()
        self.setMinimumSize(1, 50)
        self.setScaledContents(False)

    def setPixmap(self, pixmap):
        self.pix = pixmap
        super().setPixmap(self.scaledPixmap())

    def heightForWidth(self, width):
        if self.pix.isNull():
            return self.height()
        else:
            return self.pix.height() * width / self.pix.width()

    def sizeHint(self):
        w = self.width()
        return QSize(w, self.heightForWidth(w))

    def scaledPixmap(self):
        return self.pix.scaled(self.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                               QtCore.Qt.TransformationMode.SmoothTransformation)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        if not self.pix.isNull():
            super().setPixmap(self.scaledPixmap())


class WeatherWidget(QFrame, Ui_Form):
    """
        The main class for the weather widget (the ui parts are defined above in Ui_Form)
    """
    def __init__(self, parent=None):
        super(WeatherWidget, self).__init__(parent)
        self.setupUi(self)

    def update_data(self, weather_measurement, is_day=True):
        """
        Updates the data in the widget with the one from a new measurement
        :param weather_measurement: WeatherMeasurement object containing data
        :param is_day: Attribute of the widget if it is on the days page or
        hours page (the only code difference is that the hours page also displays an hour, not only the date of the
        measurement)
        :return: Nothing
        """
        # Updates the date field
        if is_day:
            self.dateLabel.setText(weather_measurement.day)
        else:
            self.dateLabel.setText(weather_measurement.day + ' ' + weather_measurement.time)

        # Updates the text fields with data from the measurement
        self.temperatureLabel.setText(str(math.ceil(weather_measurement.temperature_min)) + "°C - " +
                                      str(math.ceil(weather_measurement.temperature_max)) + "°C")
        self.precipitationLabel.setText(str(int(weather_measurement.precipitation_chance * 100)) + " % Rain chance")
        self.pressureLabel.setText(str(math.floor(weather_measurement.pressure)) + " mb Press.")
        self.humidityLabel.setText(str(math.floor(weather_measurement.humidity)) + "% Hum.")
        self.windSpeedLabel.setText("Wind: " + str(round(weather_measurement.wind_speed, 2)) + "m/s")
        self.windDirectionLabel.setText(str(math.floor(weather_measurement.wind_dir)) + "° dir.")

        # Gets the description from the measurement and updates the image mostly related to it
        description = weather_measurement.description

        if 'few clouds' in description:
            cloud_image = QPixmap("./data/icons/cloud-sunny.png")
            self.imageWidget.setPixmap(cloud_image)
        if 'cloud' in description:
            cloud_image = QPixmap("./data/icons/cloudy.png")
            self.imageWidget.setPixmap(cloud_image)
        elif 'rain' in description:
            rain_image = QPixmap("./data/icons/rain.png")
            self.imageWidget.setPixmap(rain_image)
        elif 'snow' in description:
            snow_image = QPixmap("./data/icons/snow.png")
            self.imageWidget.setPixmap(snow_image)
        elif 'thunderstorm' in description:
            thunderstorm_image = QPixmap("./data/icons/thunderstorm.png")
            self.imageWidget.setPixmap(thunderstorm_image)
        else:
            sunny_image = QPixmap("./data/icons/sunny.png")
            self.imageWidget.setPixmap(sunny_image)

