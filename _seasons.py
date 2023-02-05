'''checking current season'''
from datetime import datetime

class Season():
    '''class representation of the season'''
    def __init__(self, latitude, mean_temperature):
        self.latitude = latitude
        self.mean_temperature = mean_temperature

    def check(self):
        '''method used to check current season'''
        if self.latitude >0: #northen hemisphere
            if self.mean_temperature <=0:
                season = 'winter'
            elif self.mean_temperature >0 and \
                self.mean_temperature <= 5 and \
                datetime.now().month in (10,11,12):
                season = 'early winter'
            elif self.mean_temperature >0 and \
                self.mean_temperature <= 5 and \
                datetime.now().month in (1,2,3):
                season = 'early spring'
            elif self.mean_temperature >5 and \
                self.mean_temperature <= 10 and \
                    datetime.now().month in (1,2,3,4,5,6):
                season = 'spring'
            elif self.mean_temperature >10 and \
                self.mean_temperature <= 16 and \
                    datetime.now().month in (1,2,3,4,5,6):
                season = 'late spring'
            elif self.mean_temperature >16:
                season = 'summer'
            elif self.mean_temperature <=16 and \
                self.mean_temperature > 13 and \
                    datetime.now().month in (7,8,9,10,11,12):
                season = 'late summer'
            elif self.mean_temperature <=13 and \
                self.mean_temperature > 10 and \
                    datetime.now().month in (7,8,9,10,11,12):
                season = 'early fall'
            elif self.mean_temperature <=10 and \
                self.mean_temperature > 5 and \
                    datetime.now().month in (7,8,9,10,11,12):
                season = 'fall'
        else: #southern hemisphere
            if self.mean_temperature <= 0:
                season = 'winter'
            elif self.mean_temperature >0 and \
                self.mean_temperature <= 5 and \
                datetime.now().month in (4,5,6):
                season = 'early winter'
            elif self.mean_temperature >0 and \
                self.mean_temperature <= 5 and \
                datetime.now().month in (7,8,9):
                season = 'early spring'
            elif self.mean_temperature >5 and \
                self.mean_temperature <= 10 \
                    and datetime.now().month in (7,8,9,10,11,12):
                season = 'spring'
            elif self.mean_temperature >10 and \
                self.mean_temperature <= 16 \
                    and datetime.now().month in (7,8,9,10,11,12):
                season = 'late spring'
            elif self.mean_temperature >16:
                season = 'summer'
            elif self.mean_temperature <=16 and \
                self.mean_temperature > 13 \
                    and datetime.now().month in (1,2,3,4,5,6):
                season = 'late summer'
            elif self.mean_temperature <=13 and \
                self.mean_temperature > 10 and \
                    datetime.now().month in (1,2,3,4,5,6):
                season = 'early fall'
            elif self.mean_temperature <=10 \
                and self.mean_temperature > 5 \
                    and datetime.now().month in (1,2,3,4,5,6):
                season = 'fall'
        return season
    