#!/usr/local/bin/python3
from requests import get
from json import loads
json = loads(get('https://rickandmortyapi.com/api/character/' + input('Enter a character ID: ')).text)
print('\n'.join(map(lambda key: key.capitalize() + ': ' + json[key]
    , ['name','status','species','gender'])) + \
    '\nLocation: ' + json['location']['name'] + \
    '\nEpisode' + ('s: ' if len(episodes := json['episode']) > 1 else ': ') + \
        ', '.join(map(lambda n: n[40:], episodes)))
