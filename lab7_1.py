#!/usr/local/bin/python3
from requests import get
from json import loads
json = loads(get('http://api.openweathermap.org/data/2.5/weather?appid=3ddf6ac5a114b2df2ef796cac6796878&q=' + input('Enter a city name: ')).text)
print('Weather: ' + \
    (weather := json['weather'][0])['main'] + ', ' + weather['description'] + \
    '\nHumidity: ' + str((main := json['main'])['humidity']) + \
    '%\nPressure: ' + str(main['pressure']))
