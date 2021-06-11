'''This documentation involves importing a json file and converting it into a python object'''

import json

with open('country_by_capital.json') as f:
    data = json.load(f)

for country in data:
    print(country)
