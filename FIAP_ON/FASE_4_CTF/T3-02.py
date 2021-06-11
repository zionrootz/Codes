#coloquei o import requests
import requests


r = requests.get('https://swapi.dev/api/people/1')

json = r.json()

print(json['height'])