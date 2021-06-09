import json

people_string = '''
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

data = json.loads(people_string)
print(data) 

print(data['people'])

for i in data['people']:
    print(i['name'])