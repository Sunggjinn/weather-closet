from flask import Flask, render_template, request
from werkzeug.utils import redirect
from scrapper import weather_search

app = Flask("Weather Scrapper")


@app.route("/")
def home():
    area = request.args.get('area')
    if area:
        weather = weather_search(area)
        print(weather)
    return render_template("index.html", searchingBy=area)


app.run ('0.0.0.0', port=5000)
