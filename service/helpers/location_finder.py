from geopy.geocoders import Nominatim


class LocationFinder:
    def __init__(self):
        self.__geolocator = Nominatim(user_agent='MyWeather')

    def locate_city(self, city_name):
        location = self.__geolocator.geocode(city_name, language='en')
        location_data = dict()
        location_data['country'] = location.raw['display_name'].split(',')[-1].strip()
        location_data['name'] = location_data['city'] = city_name
        location_data['latitude'] = float(location.raw['lat'])
        location_data['longitude'] = float(location.raw['lon'])
        return location_data
