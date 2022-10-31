from fastapi import HTTPException, status

import requests
api = "e2cf5921e72b5d355b06dd22324c75b7"

def checkCurrentWeather(search):
    check = f"http://api.positionstack.com/v1/forward?access_key={api}&query={search}"
    country = requests.get(check).json()["data"][0]

    long = country["longitude"]
    latt = country["latitude"]

    #IBM
    apiKey = "1bbf9714b9ac4babbf9714b9acebabca"
    url_forcast_now = f"https://api.weather.com/v1/geocode/{latt}/{long}/forecast/nowcast.json?language=en-US&units=e&apiKey={apiKey}"
    
    if requests.get(url_forcast_now).status_code == 204:
        raise HTTPException(status_code=status.HTTP_401,
        detail="No weather info")
    return requests.get(url_forcast_now).json()
    