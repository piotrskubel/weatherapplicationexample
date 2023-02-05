'''solving possible problems'''
from datetime import datetime
from geopy.geocoders import Nominatim, GeocoderNotFound
from meteostat import Point, Normals
import pandas as pd
from _normals import adjust_normals

class Place():
    '''class made to represent correct location'''
    def __init__(self, city):
        self.city = city
    def validate_location(self):
        '''method checking if given location is correct'''
        geolocator = Nominatim(user_agent='weather app test')
        if geolocator.geocode(self.city) is None:
            location = None
        else:
            location = geolocator.geocode(self.city)
        return location

class Coordinates():
    '''class made to represent correct location coordinates'''
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def adjust(self):
        '''method searching nearest coordinates for which temperature normals exist'''
        latitude : float = self.latitude
        longitude: float = self.longitude
        LAT_UP = latitude+1.2
        LON_RIGHT = longitude+1.2
        LAT_DOWN = latitude-1.2
        LON_LEFT = longitude-1.2
        @staticmethod
        def try_to_get_normals(latitude, longitude):
            '''method trying to get temperature normals for given coordinates'''
            place = Point(latitude, longitude)
            data_geo = Normals(place,1991,2020)
            data_geo = data_geo.fetch()
            data_geo = pd.DataFrame(data_geo)
            return data_geo
        data_geo = try_to_get_normals(latitude, longitude)
        try:
            while data_geo.empty and longitude > LON_LEFT:
                longitude-=0.15
                data_geo = try_to_get_normals(latitude, longitude)
                while data_geo.empty and latitude > LAT_DOWN:
                    latitude-=0.15
                    data_geo = try_to_get_normals(latitude, longitude)
                    while data_geo.empty and longitude < LON_RIGHT:
                        longitude+=0.15
                        data_geo = try_to_get_normals(latitude, longitude)
                        while data_geo.empty and latitude < LAT_UP and LON_LEFT < longitude:
                            latitude+=0.15
                            longitude-=0.15
                            data_geo = try_to_get_normals(latitude, longitude)
        except SyntaxError:
            pass
        history_max = pd.Series(data_geo.get('tmax'))
        history_min = pd.Series(data_geo.get('tmin'))
        history_avg = pd.Series(data_geo.get('tavg'))

        check_month = datetime.now().month
        if check_month == 12:
            next_month = 1
            previous_month = check_month-1
        elif check_month == 1:
            previous_month = 12
            next_month = check_month+1
        else:
            next_month = check_month+1
            previous_month = check_month-1
        try:
            history_list = []
            previous = history_max.pop((previous_month))
            current = history_max.pop(check_month)
            future = history_max.pop((next_month))
            adjust_normals(previous, current, future, history_list)
            previous = history_min.pop((previous_month))
            current = history_min.pop(check_month)
            future = history_min.pop((next_month))
            adjust_normals(previous, current, future, history_list)
            previous = history_avg.pop((previous_month))
            current = history_avg.pop(check_month)
            future = history_avg.pop((next_month))
            adjust_normals(previous, current, future, history_list)
        except IndexError or KeyError or GeocoderNotFound:
            history_list = [None]*8

        return history_list
