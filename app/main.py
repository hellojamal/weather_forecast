#! /urs/bin/env python flask
# _*_ coding: utf-8

# project initial file


from flask import jsonify, render_template, Flask, request
import requests
from load_json import load_json


CITY_DICT = load_json()

# create a Flask application
app = Flask(__name__)


# define root route
@app.route('/')
def data():
    """get default weather function"""
    resp = requests.get("http://t.weather.itboy.net/api/weather/city/101010100")
    data = resp.json()
    return render_template("index2.html", data=data)


# define query route
@app.route("/query", methods=["POST"])
def query():
    """get weather function"""
    data = request.json
    city = data.get("query", "")
    city_code = CITY_DICT.get(city, None)
    print("city:", city, "city_code", city_code)
    if city_code is not None:
        api_weather = " http://t.weather.itboy.net/api/weather/city/"
        url = api_weather + city_code
        print("url:", url)
        res = requests.get(url=url).json()
    else:
        res = {"code": 404}
    print(res)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
