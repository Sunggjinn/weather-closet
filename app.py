from flask import Flask, render_template, request
from werkzeug.utils import redirect
from scrapper import get_weather

app = Flask ("Weather Scrapper")


@app.route ("/")
def home():
    return render_template ("index.html")


@app.route ("/report")
def report():
    area = request.args.get('area')
    if area:
        area = area.lower()
        weathers = get_weather(area)
        print(weathers)
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=area)


app.run ('0.0.0.0', port=5000)
