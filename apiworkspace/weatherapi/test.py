from flask import Flask, render_template, request
# send requests to any url
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zip']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=ee996ef995fbd8f259b8d3bd512fccba')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_f = (temp_k - 273.15) * 1.8 + 32
	return render_template('temperature.html', temp=temp_f)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
