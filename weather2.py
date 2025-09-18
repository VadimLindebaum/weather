import requests

# Tallinna koordinaadid
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.437&lon=24.7536"

# Yr API nõuab User-Agent headerit (pane siia enda nimi või projekti nimi)
headers = {"User-Agent": "IlmaHarjutus/1.0"}

response = requests.get(url, headers=headers)
data = response.json()

# Võtame timeseries listi
timeseries = data["properties"]["timeseries"]

# Prindime esimesed 5 kirjet
for entry in timeseries[:5]:
    time = entry["time"]
    temp = entry["data"]["instant"]["details"]["air_temperature"]
    print(f"{time} {temp}C")
