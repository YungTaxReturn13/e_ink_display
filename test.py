import pandas as pd
import requests
import json

x = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&appid=938475897942d64ec188f455197036f5&units=imperial"
)

y = json.loads(x.text)
print(y["current"])
