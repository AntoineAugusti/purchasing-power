import json
import datetime

import requests
import pycountry

results = {}
for country in pycountry.countries:
    code = country.alpha_2

    url = f"https://api.purchasing-power-parity.com/?target={code}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    if "ppp" in data:
        print(f"Got data for {code}")
        results[code] = data["ppp"]

filename = datetime.date.today().strftime("%Y-%m-%d")
with open(f"data/{filename}.json", "w") as f:
    json.dump(results, f)
