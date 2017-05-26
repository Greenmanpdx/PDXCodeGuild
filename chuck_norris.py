import requests

# r = requests.get('http://api.icndb.com/jokes/random')
#
# data = r.json()
# print(data['value']['joke'])

"""
As a user I want to be able to enter my city or zip code
and recieve my temp in C or F.

As a user I want to know what condition it is outside.
"""

import requests



package = {
    'APPID': "9ef3311b380d2586bf47ff522529e7a9",
}

query = input('Check the temperature \n'
              '1. by city \n'
              '2. by zip code \n')

if query == '1':
    city = input('Eneter the city: ')
    package['q'] = city
if query == '2':
    zip_code = input('Enter the zipcode: ')
    package['zip'] = zip_code

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

json_data = r.json()

print(r.url)
kelvins = json_data['main']['temp']
temp_type = input('Which format? \n'
                  '1. Celcius \n'
                  '2. Farenheit \n')
if temp_type == '1':
    temperature = str(format((kelvins - 273), '.2f')) + ' c'
if temp_type == '2':
    temperature = str(format((1.8 * (kelvins - 273) + 32), '.2f')) + ' f'
print(temperature)