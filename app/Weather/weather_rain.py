import requests
import json

api = "e2cf5921e72b5d355b06dd22324c75b7"

def checkRainFall(search):
    check = f"http://api.positionstack.com/v1/forward?access_key={api}&query={search}"
    country = requests.get(check).json()["data"][0]

    long = country["longitude"]
    latt = country["latitude"]

    #IBM
    apiKey = "1bbf9714b9ac4babbf9714b9acebabca"
    url_rain = f"https://api.weather.com/v1/geocode/{latt}/{long}/forecast/wwir.json?language=en-US&units=e&apiKey={apiKey}"
    header = {"accept": "application/json"}

    res = requests.get(url_rain, headers=header).json()
    
    longitude = res["metadata"]["longitude"]
    latitude = res["metadata"]["latitude"]
    class_type = res["forecast"]["class"]
    phrase = res["forecast"]["phrase"]
    terse_phrase = res["forecast"]["terse_phrase"]
    fcst_valid_local = res["forecast"]["fcst_valid_local"]
    time_zone_abbrv = res["forecast"]["time_zone_abbrv"]
    precip_time_12hr = res["forecast"]["precip_time_12hr"]
    precip_day = res["forecast"]["precip_day"]

    return {"longitude": longitude, "latitude": latitude, "class_type": class_type, "phrase": phrase, "terse_phrase": terse_phrase, "fcst_valid_local": fcst_valid_local, "time_zone_abbrv": time_zone_abbrv, "precip_time_12hr": precip_time_12hr, "precip_day": precip_day,}
# print(checkRainFall(search="Ghana", state="Accra"))
