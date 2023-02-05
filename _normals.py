'''used for creating historical temperature lists'''
from datetime import datetime
from calendar import isleap

def adjust_normals(previous, current, future, history_list):
    '''adjusting temperature normals'''
    check_day = datetime.now().day
    start_temp = (previous+current)/2
    end_temp = (current+future)/2
    temp_range = abs(start_temp-end_temp)

    if datetime.now().month in [1,3,5,7,8,10,12]:
        days=31
        temp_change = 1/days*temp_range
        if previous > current:
            today_temp = start_temp-check_day*temp_change
            temporary_list = [today_temp, today_temp-temp_change, today_temp-temp_change*2 \
                , today_temp-temp_change*3, today_temp-temp_change*4, today_temp-temp_change*5 \
                    , today_temp-temp_change*6, today_temp-temp_change*7]
        else:
            today_temp = start_temp+check_day*temp_change
            temporary_list = [today_temp, today_temp+temp_change, today_temp+temp_change*2 \
                , today_temp+temp_change*3, today_temp+temp_change*4, today_temp+temp_change*5 \
                    , today_temp+temp_change*6, today_temp+temp_change*7]

    if datetime.now().month in [4,6,9,11]:
        days=30
        temp_change = 1/days*temp_range
        if previous > current:
            today_temp = start_temp-check_day*temp_change
            temporary_list = [today_temp, today_temp-temp_change, today_temp-temp_change*2 \
                , today_temp-temp_change*3,today_temp-temp_change*4, today_temp-temp_change*5 \
                    , today_temp-temp_change*6, today_temp-temp_change*7]
        else:
            today_temp = start_temp+check_day*temp_change
            temporary_list = [today_temp, today_temp+temp_change, today_temp+temp_change*2 \
                , today_temp+temp_change*3, today_temp+temp_change*4, today_temp+temp_change*5 \
                    , today_temp+temp_change*6, today_temp+temp_change*7]

    if datetime.now().month in [2] and isleap(datetime.now().year):
        days=29
        temp_change = 1/days*temp_range
        if previous > current:
            today_temp = start_temp-check_day*temp_change
            temporary_list = [today_temp, today_temp-temp_change, today_temp-temp_change*2 \
                , today_temp-temp_change*3, today_temp-temp_change*4, today_temp-temp_change*5 \
                    , today_temp-temp_change*6, today_temp-temp_change*7]
        else:
            today_temp = start_temp+check_day*temp_change
            temporary_list = [today_temp, today_temp+temp_change, today_temp+temp_change*2 \
                , today_temp+temp_change*3, today_temp+temp_change*4, today_temp+temp_change*5 \
                    , today_temp+temp_change*6, today_temp+temp_change*7]

    if datetime.now().month in [2] and (isleap(datetime.now().year)) is False:
        days=28
        temp_change = 1/days*temp_range
        if previous > current:
            today_temp = start_temp-check_day*temp_change
            temporary_list = [today_temp, today_temp-temp_change, today_temp-temp_change*2 \
                , today_temp-temp_change*3, today_temp-temp_change*4, today_temp-temp_change*5 \
                    , today_temp-temp_change*6, today_temp-temp_change*7]
        else:
            today_temp = start_temp+check_day*temp_change
            temporary_list = [today_temp, today_temp+temp_change, today_temp+temp_change*2 \
                , today_temp+temp_change*3,today_temp+temp_change*4, today_temp+temp_change*5 \
                    , today_temp+temp_change*6, today_temp+temp_change*7]
    history_list.append(temporary_list)
