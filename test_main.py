'''testing main functionalities'''
from click.testing import CliRunner
from main import main

def test_main_now():
    '''testing current weather for existing place'''
    runner = CliRunner()
    result = runner.invoke(main,['-n', 'Wrocław'])
    assert result.exit_code == 0

def test_main_forecast():
    '''testing forecast for existing place'''
    runner = CliRunner()
    result = runner.invoke(main,['-f', 'Wrocław'])
    assert result.exit_code == 0

def test_main_anomaly():
    '''testing anomalies for existing place'''
    runner = CliRunner()
    result = runner.invoke(main,['-a', 'Wrocław'])
    assert result.exit_code == 0

def test_main_warning():
    '''testing alert for existing place'''
    runner = CliRunner()
    result = runner.invoke(main,['-w', 'Wrocław'])
    assert result.exit_code == 0

def test_main_incorrect_place():
    '''testing all the options for non-existing place'''
    runner = CliRunner()
    result = runner.invoke(main,['-n', '-f', '-a', '-w', '.asjkbcjkdasnclkd'])
    assert result.exception

def test_main_hard_to_reach_place():
    '''testing all the options for hard-to-reach existing place'''
    runner = CliRunner()
    result = runner.invoke(main,['-a', 'Grytviken'])
    result_2 = runner.invoke(main,['-n', '-f', '-w', 'Grytviken'])
    assert result.exception
    assert result_2.exit_code == 0
