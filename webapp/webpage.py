from fileinput import filename
from re import template
from flask import Flask, render_template, url_for
from graphviz import render
import json
from datetime import datetime
from wind_speed import wind_speed_categories
from convert_timezones import utc_to_est
import random
import qrcode
import os

qr_folder = "information/qr_codes"
app = Flask(__name__)
app.config["qr_folder"] = qr_folder


with open("information/ny_times.json") as json_file:
    news_data = json.load(json_file)

with open("information/weather.json") as json_file:
    weather_data = json.load(json_file)

# Getting the time everything was generated based on the weather data timestamp
my_datetime_est = utc_to_est(weather_data["current"]["dt"], "%Y-%m-%d %H:%M:%S %Z%z")

# Converting Sunrise time from utc to est
sunrise = utc_to_est(weather_data["current"]["sunrise"], "%H:%M:%S")

# Converting Sunset time from utc to est
sunset = utc_to_est(weather_data["current"]["sunset"], "%H:%M:%S")

current_weather = {
    "sunrise": sunrise,
    "sunset": sunset,
    "tempurature": weather_data["current"]["temp"],
    "feels_like": weather_data["current"]["feels_like"],
    "wind_speed": wind_speed_categories(weather_data["current"]["wind_speed"]),
    "conditions": weather_data["current"]["weather"][0]["description"].title(),
}

forecast = []
for i in weather_data["daily"]:
    forecast.append(
        {
            "date": utc_to_est(i["dt"], "%a %m/%d"),
            "high": i["temp"]["max"],
            "low": i["temp"]["min"],
            "weather": i["weather"][0]["main"],
        }
    )


@app.route("/news")
def news():
    x = random.randint(0, len(news_data["results"]) - 1)
    story_data = news_data["results"][x]

    input_data = news_data["results"][x]["url"]
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(f"webapp/static/qrcode{x}.png")
    qr_images = url_for('static', filename=f'qrcode{x}.png' )

    return render_template("news.html", time=my_datetime_est, news_data=story_data, qr_images = qr_images)


@app.route("/weather")
def weather():
    dir = "webapp/static/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    return render_template(
        "weather.html",
        time=my_datetime_est,
        current_weather=current_weather,
        forecast_weather=forecast,
    )


if __name__ == "__main__":
    app.run(debug=True)
