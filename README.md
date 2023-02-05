# Getting started

You are about to use a CLI weather application example based on openweathermap.org API.
First you need to apply for a free API key: https://openweathermap.org/price.
Then download all the files and create .env file in the same directory. It will contain:
```
WEA_API={free openweathermap.org API you have applied for}
```
The application can be started by typing:
```
python main.py [OPTIONS] [CITY]
```
CITY - required argument, application will show weather data for this place
OPTIONS - at least one of the options is required, you can show available options by typing:
```
python main.py -h
```

