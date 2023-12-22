from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/result', methods = ['POST'])
def resultPage():
    city = request.form['city']

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=24bbb9c057fda5866cf7a4c73eab24c0'
    response = requests.get(url.format(city))
    # print(response)

    # location = response['name']
    temp = response['main']['temp']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    description = response['weather'][0]['description']

    return render_template('result.html', temp=temp, humidity=humidity, wind_speed=wind_speed, description=description)

if __name__ == '__main__':
    app.run()