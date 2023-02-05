'''CLI main script'''
from datetime import datetime
import click
from click import UsageError
from prettytable import PrettyTable, ALL
from _data import Weather
from _solver import Place, Coordinates
from _alerts import WeatherAlert
from _seasons import Season

@click.command(add_help_option=False)
@click.help_option('-h', '--help', help='Show available options')
@click.argument('city')
@click.option('-n', '--now', is_flag=True, show_default=True,\
default=False, help='Current conditions')
@click.option('-f', '--forecast', is_flag=True, show_default=True,\
default=False, help='7-days forecast')
@click.option('-a', '--anomaly', is_flag=True, show_default=True,\
default=False, help='2m temperature anomalies')
@click.option('-w', '--warning', is_flag=True, show_default=True,\
default=False, help='Weather alerts')
def main(city, now, forecast, anomaly, warning):
    '''CLI application showing weather conditions for given CITY,
    at least one OPTION is required'''
    location = Place(city).validate_location()
    try:
        latitude : float = location.latitude
        longitude: float = location.longitude
    except AttributeError as exc:
        raise UsageError('There is a problem with your place') from exc
    history_list = Coordinates(latitude, longitude).adjust()
    day_temperature, night_temperature, description, now_description, \
    now_temperature, real_feel, time_stamps, mean_temperature, day_max, \
    day_min, day_avg, conditions = Weather(latitude, longitude).get_conditions()
    season = Season(latitude, mean_temperature).check()
    time_list = [datetime.fromtimestamp(timestamp).strftime("%d/%m") for timestamp in time_stamps]

    def show_current_conditions():
        table = PrettyTable()
        table.add_rows([['Temperature',f'{now_temperature}℃'],
        ['Real-feel',f'{real_feel}℃'],
        ['Conditions',now_description[0]],
        ['Season',season]])
        table.hrules=ALL
        click.echo(table.get_string(header=False))

    def show_forecast():
        day_list =  [round(day+0.75) for day in day_temperature]
        night_list =  [round(night-0.75) for night in night_temperature]
        forecast_data = zip(time_list[1:],day_list[1:],night_list[1:],description[1:])
        table = PrettyTable()
        table.field_names = ['Date','Maximum temperature', 'Minimum temperature','Conditions']
        for time, day, night, conditions in forecast_data:
            table.add_row([time, day, night, conditions])
        click.echo(table)

    def show_anomalies():
        table = PrettyTable()
        table.field_names = ['Date','Maximum temperature anomaly','Minumum temperature anomaly'
        ,'Average temperature anomaly']
        try:
            anomaly_max = [f'{round(a-b,2)}℃' for a,b in zip(day_max,history_list[0])]
            anomaly_min = [f'{round(a-b,2)}℃' for a,b in zip(day_min,history_list[1])]
            anomaly_avg = [f'{round(a-b,2)}℃' for a,b in zip(day_avg,history_list[2])]
            anomaly_data = zip(time_list, anomaly_max, anomaly_min, anomaly_avg)
            for time, maxi, mini, avg in anomaly_data:
                table.add_row([time, maxi, mini, avg])
            click.echo(table)
        except TypeError as exc:
            raise UsageError('Temperature anomalies are not available for given place') from exc

    def show_alert():
        try:
            auto_alerts = conditions['alerts'][0]
        except KeyError:
            auto_alerts = None
        api_alert, alert_level = WeatherAlert(auto_alerts).retrieve()
        click.echo(click.style(f'{api_alert}', fg=alert_level))
    if not now and not forecast and not anomaly and not warning:
        click.echo('Type: python main.py -h for available options, at least one is required')
    if now:
        show_current_conditions()
    if forecast:
        show_forecast()
    if anomaly:
        show_anomalies()
    if warning:
        show_alert()
if __name__ == '__main__':
    main()
