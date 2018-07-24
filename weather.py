import urllib.request
import json

city_name = str(input("Enter city name: "))

api_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=d151c5c090c0ca461ee656b2fd17188e&units=imperial'
url = urllib.request.urlopen(api_url)
output = url.read().decode('utf-8')
api_dict = json.loads(output)
url.close()

data = dict(
	city = api_dict.get('name'),
	country = api_dict.get('sys').get('country'),
	temp = api_dict.get('main').get('temp'),
	sky = api_dict['weather'][0]['main'],
	clouds = api_dict.get('clouds').get('all')
	)

print('The weather for {}, {} is {} degrees with predicted {} and {} cloud coverage.'.format(data['city'], data['country'], data['temp'], data['sky'], data['clouds']))