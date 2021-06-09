'''' THis document deals with json to python and vice versa'''

import json

PEOPLE_STRING = '''
{
    "people": [
        {
          "name": "Sree",
          "phone":123456789,
          "email":"sree@gmail.com",
          "has_license": true 
        }, 
        {
            "name": "Chicku",
            "phone":345261780,
            "email": null,
            "has_license": false
        }
    ]
}
'''

data = json.loads(PEOPLE_STRING)
print(data)

print(data['people'])

for i in data['people']:
    print(i['name'])
    