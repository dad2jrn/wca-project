import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

@app.route('/')
def method_name():
   city = 'las vegas,us'
   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=216526f7de265c4a32d3666c4012324f'
   response = requests.get(url).json()
   print(response)
   return render_template('weather.html')


if __name__ == '__main__':
 app.run()