import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def method_name():
   if request.method == 'POST':
      city = request.form.get('city')
   else:
      city = 'Los Angeles'
   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=216526f7de265c4a32d3666c4012324f'
   response = requests.get(url).json()
   weather = {
      'city': city.capitalize(),
      'temp': int(response['main']['temp']),
      'description': response['weather'][0]['description'].capitalize(),
      'icon': response['weather'][0]['icon']
   }
   return render_template('weather.html', weather=weather)


if __name__ == '__main__':
 app.run()