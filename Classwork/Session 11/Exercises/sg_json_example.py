import urllib.request
import json

APIKEY = '68b6d3a4e115c1ccccd6c47e7a52a914'
city = 'ottawa'
country_code = 'can'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'
city_upper = city.upper()

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# print(response_data)

# How do we get current temperature?

main = response_data['main']
temp = main['temp']
celsius_temp = (temp - 273.15)


print('The current temperature in', city_upper, f'is {celsius_temp:.1f} degrees celsius.')
