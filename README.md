Väga hea harjutus, Vadim! Teeme selle võimalikult lihtsaks ja arusaadavaks. Kasutan Pythonit, kuna see on selge ja sobib hästi JSON-i töötlemiseks. Kasutame `requests` moodulit HTTP päringu tegemiseks ja `json` struktuuri lugemiseks.

---

🌍 API info

• API: `https://api.met.no/weatherapi/locationforecast/2.0/compact`
• Tallinna koordinaadid:• Latitude: 59.4370
• Longitude: 24.7536

• Vajalik on lisada User-Agent päis, muidu API ei vasta.

---

 Selgitus

• `data["properties"]["timeseries"]` on list, kus iga element sisaldab:• `"time"` – kuupäev ja kellaaeg
• `"data" → "instant" → "details" → "air_temperature"` – temperatuur antud hetkel

• Me ei töötle kuupäeva, vaid prindime otse JSON-ist.
• `[:10]` tähendab, et võtame esimesed 10 kirjet.


---

Käivitamine

1. Paigalda `requests` moodul (kui pole veel):pip install requests

2. Salvesta kood faili `weather.py`
3. Käivita:python weather.py
4. 
