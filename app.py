import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

@app.route('/')
def method_name():
   return render_template('weather.html')


if __name__ == '__main__':
 app.run()