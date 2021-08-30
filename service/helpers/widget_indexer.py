

"""
    Module for keeping the indexes of the starting widgets in the scrollable part of the app
"""


class WeatherWidgetIndexer:
    def __init__(self):
        self.__hour_index = 1
        self.__day_index = 1
        self.__indexer_methods = {"day": {-1: self.__backward_day, 1: self.__forward_day},
                                  "hour": {-1: self.__backward_hour, 1: self.__forward_hour}}

    @property
    def hour_index(self):
        return self.__hour_index

    @property
    def day_index(self):
        return self.__day_index

    def update_indexer(self, indexer_type, amount, limit):
        """
        Updates the indexer values according to the given parameters
        :param indexer_type: 'day' or 'hour'
        :param amount: -1 (backward) or 1 (forward)
        :param limit: Upper limit of the indexer
        :return: True if the indexer was updated, False otherwise
        """
        if indexer_type not in ['day', 'hour']:
            raise Exception('Indexer type is invalid')
        if amount not in [-1, 1]:
            raise Exception('Amount is invalid')
        return self.__indexer_methods[indexer_type][amount](limit)

    def __forward_day(self, day_limit=7):
        if self.__day_index + 3 >= day_limit:
            return False
        else:
            self.__day_index += 1
            return True

    def __backward_day(self, day_limit=1):
        if self.__day_index == 1:
            return False
        else:
            self.__day_index -= 1
            return True

    def __forward_hour(self, hour_limit=10):
        if self.__hour_index + 3 >= hour_limit:
            return False
        else:
            self.__hour_index += 1
            return True

    def __backward_hour(self, hour_limit=1):
        if self.__hour_index == 1:
            return False
        else:
            self.__hour_index -= 1
            return True

    def reset_indexer(self):
        self.__day_index = self.__hour_index = 1
