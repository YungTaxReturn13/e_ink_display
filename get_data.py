import requests
import json


def get_data():
    zip_code = 22152

    with open("keys/ny_times.txt") as f:
        ny_times_key = f.read()

    with open("keys/open_weather_map.txt") as f:
        weather_key = f.read()

    x = requests.get(
        f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},us&appid={weather_key}"
    )
    lat = x.json()["lat"]
    lon = x.json()["lon"]
    city = x.json()["name"]

    x = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={weather_key}&units=imperial"
    )
    weather_json = x.json()
    with open("information/weather.json", "w") as f:
        json.dump(weather_json, f)

    x = requests.get(
        f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={ny_times_key}"
    )
    ny_times_json = x.json()
    with open("information/ny_times.json", "w") as f:
        json.dump(ny_times_json, f)


if __name__ == "__main__":
    get_data()
