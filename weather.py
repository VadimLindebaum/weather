import requests

# Tallinna koordinaadid
lat = 59.4370
lon = 24.7536

# API URL koos parameetritega
url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"

# HTTP päring koos User-Agent päisega
headers = {
    "User-Agent": "TallinnWeatherApp/1.0 vadim@example.com"
}

response = requests.get(url, headers=headers)

# Kontrolli, kas päring õnnestus
if response.status_code != 200:
    print("Päring ebaõnnestus:", response.status_code)
    exit()

# JSON andmete laadimine
data = response.json()

# Liigu timeseries listi
timeseries = data["properties"]["timeseries"]

# Väljasta esimesed 10 kirjet (või rohkem, kui soovid)
for entry in timeseries[:10]:
    time = entry["time"]
    temperature = entry["data"]["instant"]["details"]["air_temperature"]
    print(f"{time} {temperature}C")
