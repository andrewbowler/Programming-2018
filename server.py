import urllib.request
import json
from flask import Flask

app = Flask(__name__)

@app.route('/weather/<city_name>')
def index(city_name):
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

	return 'The weather for {}, {} is {} degrees with predicted {} and {} percent cloud coverage.'.format(data['city'], data['country'], data['temp'], data['sky'], data['clouds'])

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 3000)