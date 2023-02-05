'''weather alerts'''
from datetime import datetime

class WeatherAlert():
    '''WeatherAlert class which uses current session alerts'''
    def __init__(self, auto_alerts):
        self.auto_alerts = auto_alerts

    def retrieve(self):
        '''method used to retrieve an alert'''
        if self.auto_alerts is not None:
            valid = datetime.fromtimestamp(self.auto_alerts['start']).strftime('%d/%m/%Y %H:%M')
            expires = datetime.fromtimestamp(self.auto_alerts['end']).strftime('%d/%m/%Y %H:%M')
            try:
                content = str(self.auto_alerts['description'][0]).lower()+\
                str(self.auto_alerts['description'][1:])
            except IndexError:
                content = self.auto_alerts['event']

            api_alert = f'From {valid} to {expires} {content}'
            level = str(self.auto_alerts['event'])
            if 'Red' in level or 'red' in level:
                alert_level = 'red'
            elif 'Orange' in level or 'orange' in level:
                alert_level = 'bright_red'
            else:
                alert_level = 'yellow'
        else:
            api_alert = 'There is no alert for given place'
            alert_level = None
        return api_alert, alert_level
