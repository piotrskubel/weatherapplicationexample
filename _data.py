'''data collector'''
import json
from decouple import config
import requests
from requests import ReadTimeout
from click import UsageError
import numpy as np

class Weather():
    '''class containing weather conditions'''
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_conditions(self):
        '''method used to get required conditions'''
        WEA_API = config('WEA_API')
        day_temperature = [] #daily forecast
        night_temperature = []
        evening_temperature = []
        morning_temperature = []
        description = []
        time_stamps = []
        now_description = [] #current conditions
        url= f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&units=metric&exclude=minutely,hourly&appid={WEA_API}"
        try:
            get_url = requests.get(url, timeout=7)
        except ReadTimeout as exc:
            raise UsageError('Cannot connect to the weather API') from exc
        conditions = json.loads(get_url.text)
        now = conditions['current']
        now_weather = now['weather']
        now_temperature = round(now['temp']) #current temperature
        real_feel = round(now['feels_like']) #current real-feel
        for now in now_weather:
            now_list = now['description']
            now_description.append(now_list)
        data = conditions['daily']
        for entry in data:
            time_stamps.append((entry).get('dt'))
            temp = entry['temp']
            if 'day' in temp:
                day_temperature.append((temp).get('day'))
            if 'night' in temp:
                night_temperature.append((temp).get('night'))
            if 'eve' in temp:
                evening_temperature.append((temp).get('eve'))
            if 'morn' in temp:
                morning_temperature.append((temp).get('morn'))
            weather = entry['weather']
            for double_u in weather:
                desc = double_u['description']
                description.append(desc)
        day_mean: float = np.average(day_temperature)
        night_mean: float = np.average(night_temperature)
        eve_mean: float = np.average(evening_temperature)
        morn_mean: float = np.average(morning_temperature)
        mean_temperature: float = (day_mean+night_mean+eve_mean+morn_mean)/4
        day_max = [round(num+0.75) for num in day_temperature]
        day_min = [round(num-0.75) for num in night_temperature]
        day_avg = [(n+m+d+e)/4 for n,m,d,e in zip \
        (night_temperature, morning_temperature, day_temperature, evening_temperature)]

        return day_temperature, night_temperature, \
        description, now_description, now_temperature, real_feel, time_stamps,\
        mean_temperature, day_max, day_min, day_avg, conditions
