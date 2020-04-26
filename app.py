from flask import Flask, render_template, request
from werkzeug.utils import redirect
from scrapper import weather_search

app = Flask("Weather Scrapper")


@app.route("/")
def home():
    area = request.args.get('area')
    if area:
        weather_element = weather_search(area)
        print(weather_element)
    return render_template("index.html", searchingBy=area, today_temp=weather_element[0], high_temp=weather_element[3], low_temp=weather_element[2])


app.run ('0.0.0.0', port=5000)
