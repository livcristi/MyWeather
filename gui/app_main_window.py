from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow

from gui.weather_widget import WeatherWidget

"""
    Module for the main window GUI. The GUI consists of a stacked widget with two parts: the part for daily weather
    forecasts and one for hourly forecasts. Each one contains multiple weather widgets and the data can be scrolled
    using two side buttons (for back and forward)
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Initialises the main window design (This was automatically generated using the pyuic5 library)
        :param MainWindow: QT Designer object
        :return: Nothing
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{background-color:  rgb(255, 247, 233);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QWidget#tab{\n"
                                     "ont: 9pt \"Bahnschrift\";\n"
                                     "background-color: qlineargradient(spread:pad, x1:0.438, y1:0, x2:0.418, y2:1, "
                                     "stop:0.120192 rgba(196, 201, 202, 255), stop:0.346154 rgba(218, 255, 255, 255), "
                                     "stop:0.653846 rgba(144, 197, 195, 255), stop:0.899038 rgba(196, 255, 255, "
                                     "255));\n "
                                     "    border-width: 2px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: silver;\n"
                                     "}\n"
                                     "\n"
                                     "QWidget#tab_2{\n"
                                     "ont: 9pt \"Bahnschrift\";\n"
                                     "background-color: qlineargradient(spread:pad, x1:0.438, y1:0, x2:0.418, y2:1, "
                                     "stop:0.120192 rgba(196, 201, 202, 255), stop:0.346154 rgba(218, 255, 255, 255), "
                                     "stop:0.653846 rgba(144, 197, 195, 255), stop:0.899038 rgba(196, 255, 255, "
                                     "255));\n "
                                     "    border-width: 2px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: silver;\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget\n"
                                     "{\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.weatherToday = WeatherWidget(self.tab)
        self.weatherToday.setObjectName("weatherToday")
        self.horizontalLayout_4.addWidget(self.weatherToday)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cityLabel = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cityLabel.sizePolicy().hasHeightForWidth())
        self.cityLabel.setSizePolicy(sizePolicy)
        self.cityLabel.setStyleSheet("font: 10pt \"Bahnschrift SemiBold\";\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "border-style: solid;\n"
                                     "border-width: 2px;\n"
                                     "border-radius: 10px;\n"
                                     "border-color: rgb(49, 49, 49);")
        self.cityLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.cityLabel.setObjectName("cityLabel")
        self.verticalLayout_3.addWidget(self.cityLabel)
        self.daysWeatherWidgets = QtWidgets.QWidget(self.tab)
        self.daysWeatherWidgets.setObjectName("daysWeatherWidgets")
        self.daysWeatherWidgets.setStyleSheet("#daysWeatherWidgets{border-style: solid;\n"
                                              "border-width: 2px;\n"
                                              "border-radius: 10px;\n"
                                              "border-color: rgb(49, 49, 49);}")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.daysWeatherWidgets)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.backwardButton = QtWidgets.QPushButton(self.daysWeatherWidgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backwardButton.sizePolicy().hasHeightForWidth())
        self.backwardButton.setSizePolicy(sizePolicy)
        self.backwardButton.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.937, cy:0.488, radius:1, fx:0.00961538, fy:0.494, "
            "stop:0.129808 rgba(9, 98, 169, 255), stop:1 rgba(255, 255, 255, 255));\n "
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-radius: 10px;\n"
            "    border-color: rgb(49, 49, 49);\n"
            "")
        self.backwardButton.setText("")
        self.backwardButton.setObjectName("backwardButton")
        self.verticalLayout_6.addWidget(self.backwardButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 5)
        self.verticalLayout_6.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.dayWeatherWidget2 = WeatherWidget(self.daysWeatherWidgets)
        self.dayWeatherWidget2.setObjectName("dayWeatherWidget2")
        self.horizontalLayout_5.addWidget(self.dayWeatherWidget2)
        self.dayWeatherWidget3 = WeatherWidget(self.daysWeatherWidgets)
        self.dayWeatherWidget3.setObjectName("dayWeatherWidget3")
        self.horizontalLayout_5.addWidget(self.dayWeatherWidget3)
        self.dayWeatherWidget4 = WeatherWidget(self.daysWeatherWidgets)
        self.dayWeatherWidget4.setObjectName("dayWeatherWidget4")



        self.horizontalLayout_5.addWidget(self.dayWeatherWidget4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.forwardButton = QtWidgets.QPushButton(self.daysWeatherWidgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardButton.sizePolicy().hasHeightForWidth())
        self.forwardButton.setSizePolicy(sizePolicy)
        self.forwardButton.setStyleSheet("    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: rgb(49, 49, 49);\n"
                                         "background-color: qradialgradient(spread:pad, cx:0.063, cy:0.488, radius:1, fx:0.984044, fy:0.494, stop:0.129808 rgba(9, 98, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "")
        self.forwardButton.setText("")
        self.forwardButton.setIconSize(QtCore.QSize(20, 20))
        self.forwardButton.setObjectName("forwardButton")
        self.verticalLayout_7.addWidget(self.forwardButton)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 5)
        self.verticalLayout_7.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(2, 5)
        self.horizontalLayout_5.setStretch(3, 5)
        self.verticalLayout_3.addWidget(self.daysWeatherWidgets)
        self.auxLabel = QtWidgets.QLabel(self.tab)
        self.auxLabel.setText("")
        self.auxLabel.setObjectName("auxLabel")
        self.verticalLayout_3.addWidget(self.auxLabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 18)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.weatherNow = WeatherWidget(self.tab_2)
        self.weatherNow.setObjectName("weatherNow")
        self.horizontalLayout_7.addWidget(self.weatherNow)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 8)
        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.hourCityLabel = QtWidgets.QLabel(self.tab_2)
        self.hourCityLabel.setStyleSheet("font: 10pt \"Bahnschrift SemiBold\";\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border-style: solid;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: rgb(49, 49, 49);")
        self.hourCityLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.hourCityLabel.setObjectName("hourCityLabel")
        self.verticalLayout_5.addWidget(self.hourCityLabel)
        self.weatherHoursWidgets = QtWidgets.QWidget(self.tab_2)
        self.weatherHoursWidgets.setObjectName("weatherHoursWidgets")
        self.weatherHoursWidgets.setStyleSheet("#weatherHoursWidgets{border-style: solid;\n"
                                              "border-width: 2px;\n"
                                              "border-radius: 10px;\n"
                                              "border-color: rgb(49, 49, 49);}")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.weatherHoursWidgets)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.backwardHourButton = QtWidgets.QPushButton(self.weatherHoursWidgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backwardHourButton.sizePolicy().hasHeightForWidth())
        self.backwardHourButton.setSizePolicy(sizePolicy)
        self.backwardHourButton.setStyleSheet(
            "    background-color: qradialgradient(spread:pad, cx:0.937, cy:0.488, radius:1, fx:0.00961538, fy:0.494, stop:0.129808 rgba(9, 98, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-radius: 10px;\n"
            "    border-color: rgb(49, 49, 49);")
        self.backwardHourButton.setText("")
        self.backwardHourButton.setObjectName("backwardHourButton")
        self.verticalLayout_8.addWidget(self.backwardHourButton)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)
        self.verticalLayout_8.setStretch(2, 1)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.hourWeatherWidget2 = WeatherWidget(self.weatherHoursWidgets)
        self.hourWeatherWidget2.setObjectName("hourWeatherWidget2")
        self.horizontalLayout_9.addWidget(self.hourWeatherWidget2)
        self.hourWeatherWidget3 = WeatherWidget(self.weatherHoursWidgets)
        self.hourWeatherWidget3.setObjectName("hourWeatherWidget3")
        self.horizontalLayout_9.addWidget(self.hourWeatherWidget3)
        self.hourWeatherWidget4 = WeatherWidget(self.weatherHoursWidgets)
        self.hourWeatherWidget4.setObjectName("hourWeatherWidget4")
        self.horizontalLayout_9.addWidget(self.hourWeatherWidget4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem12)
        self.forwardHourButton = QtWidgets.QPushButton(self.weatherHoursWidgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardHourButton.sizePolicy().hasHeightForWidth())
        self.forwardHourButton.setSizePolicy(sizePolicy)
        self.forwardHourButton.setStyleSheet("    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: rgb(49, 49, 49);\n"
                                             "background-color: qradialgradient(spread:pad, cx:0.063, cy:0.488, radius:1, fx:0.984044, fy:0.494, stop:0.129808 rgba(9, 98, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                             "")
        self.forwardHourButton.setText("")
        self.forwardHourButton.setObjectName("forwardHourButton")
        self.verticalLayout_9.addWidget(self.forwardHourButton)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem13)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 5)
        self.verticalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 5)
        self.horizontalLayout_9.setStretch(2, 5)
        self.horizontalLayout_9.setStretch(3, 5)
        self.horizontalLayout_9.setStretch(4, 1)
        self.verticalLayout_5.addWidget(self.weatherHoursWidgets)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.horizontalLayout_8.setStretch(0, 5)
        self.horizontalLayout_8.setStretch(1, 9)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.cityInputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cityInputEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.cityInputEdit.setStyleSheet("font: 10pt \"Bahnschrift\";\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(74, 74, 74);")
        self.cityInputEdit.setInputMask("")
        self.cityInputEdit.setObjectName("cityInputEdit")
        self.horizontalLayout.addWidget(self.cityInputEdit)
        self.submitCityButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitCityButton.setMinimumSize(QtCore.QSize(0, 30))
        self.submitCityButton.setStyleSheet("border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: beige;\n"
                                            "padding: 8px;\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.744, stop:0.210526 rgba(26, 173, 206, 255), stop:0.746411 rgba(179, 248, 252, 255), stop:0.971292 rgba(242, 255, 255, 255));\n"
                                            "font: 11pt \"Bahnschrift\";")
        self.submitCityButton.setObjectName("submitCityButton")
        self.horizontalLayout.addWidget(self.submitCityButton)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem18)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 3)

        self.setStyleSheet("QFrame#weatherToday{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#dayWeatherWidget2{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#dayWeatherWidget3{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#dayWeatherWidget4{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#weatherNow{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#hourWeatherWidget2{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#hourWeatherWidget3{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           "QFrame#hourWeatherWidget4{background-color: rgba(72, 72, 72, 60);\n"
                           "border: 2px solid black; \n"
                           "border-radius: 30px;}"
                           )

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cityLabel.setText(_translate("MainWindow", "City: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Weather by days"))
        self.hourCityLabel.setText(_translate("MainWindow", "City: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Weather by hours"))
        self.cityInputEdit.setPlaceholderText(_translate("MainWindow", "Change the city..."))
        self.submitCityButton.setText(_translate("MainWindow", "Submit"))


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, weather_service, parent=None):
        """
        Initializes the main window
        :param weather_service: Weather Service of the app
        :param parent: Parent widget
        """
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("MyWeather")
        self.setWindowIcon(QIcon("./data/icons/cloud-sunny.png"))
        self.__weather_service = weather_service

        # Update the weather widgets using the service data
        self.weatherToday.update_data(self.__weather_service.get_today_weather())

        days_data = self.__weather_service.get_next_days_weather()
        self.dayWeatherWidget2.update_data(days_data[0])
        self.dayWeatherWidget3.update_data(days_data[1])
        self.dayWeatherWidget4.update_data(days_data[2])

        self.weatherNow.update_data(self.__weather_service.get_now_weather(), is_day=False)

        hours_data = self.__weather_service.get_next_hours_weather()
        self.hourWeatherWidget2.update_data(hours_data[0], is_day=False)
        self.hourWeatherWidget3.update_data(hours_data[1], is_day=False)
        self.hourWeatherWidget4.update_data(hours_data[2], is_day=False)

        self.cityLabel.setText('City: ' + self.__weather_service.get_city_name())
        self.hourCityLabel.setText('City: ' + self.__weather_service.get_city_name())

        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        """
        Connect the backward and forward buttons with the signals below
        :return: Nothing
        """
        self.forwardButton.clicked.connect(self.forward_days)
        self.backwardButton.clicked.connect(self.backward_days)
        self.submitCityButton.clicked.connect(self.update_city)
        self.forwardHourButton.clicked.connect(self.forward_hours)
        self.backwardHourButton.clicked.connect(self.backward_hours)

    """
        Next slots are used when the user presses the backward and forward buttons
    """

    @pyqtSlot()
    def forward_days(self):
        days_data = self.__weather_service.update_indexer('day', 1)
        if days_data:
            self.dayWeatherWidget2.update_data(days_data[0])
            self.dayWeatherWidget3.update_data(days_data[1])
            self.dayWeatherWidget4.update_data(days_data[2])

    @pyqtSlot()
    def backward_days(self):
        days_data = self.__weather_service.update_indexer('day', -1)
        if days_data:
            self.dayWeatherWidget2.update_data(days_data[0])
            self.dayWeatherWidget3.update_data(days_data[1])
            self.dayWeatherWidget4.update_data(days_data[2])

    @pyqtSlot()
    def forward_hours(self):
        hours_data = self.__weather_service.update_indexer('hour', 1)
        if hours_data:
            self.hourWeatherWidget2.update_data(hours_data[0], is_day=False)
            self.hourWeatherWidget3.update_data(hours_data[1], is_day=False)
            self.hourWeatherWidget4.update_data(hours_data[2], is_day=False)

    @pyqtSlot()
    def backward_hours(self):
        hours_data = self.__weather_service.update_indexer('hour', -1)
        if hours_data:
            self.hourWeatherWidget2.update_data(hours_data[0], is_day=False)
            self.hourWeatherWidget3.update_data(hours_data[1], is_day=False)
            self.hourWeatherWidget4.update_data(hours_data[2], is_day=False)

    @pyqtSlot()
    def update_city(self):
        """
        Updates the city from which the forecasts are
        :return: Nothing
        """
        # Gets the user input and update the service and widgets
        city_name = self.cityInputEdit.text().strip()
        if len(city_name) >= 2:
            self.__weather_service.update_city(city_name)
            # Update widgets
            self.weatherToday.update_data(self.__weather_service.get_today_weather())
            days_data = self.__weather_service.get_next_days_weather()
            self.dayWeatherWidget2.update_data(days_data[0])
            self.dayWeatherWidget3.update_data(days_data[1])
            self.dayWeatherWidget4.update_data(days_data[2])

            self.weatherNow.update_data(self.__weather_service.get_now_weather(), is_day=False)
            hours_data = self.__weather_service.get_next_hours_weather()
            self.hourWeatherWidget2.update_data(hours_data[0], is_day=False)
            self.hourWeatherWidget3.update_data(hours_data[1], is_day=False)
            self.hourWeatherWidget4.update_data(hours_data[2], is_day=False)

            self.cityLabel.setText('City: ' + city_name)
            self.hourCityLabel.setText('City: ' + city_name)
