from fastapi import HTTPException, status
import requests

api = "e2cf5921e72b5d355b06dd22324c75b7"
url = "https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json"
apiKey = "1bbf9714b9ac4babbf9714b9acebabca"


def weatherDetail(country_: str):
    global url 
    country = requests.get(url).json()
    for x in country:
        if x["Name"].lower() == country_.lower():
            
            # #IBM
            url_weather_headlines = f"https://api.weather.com/v3/alerts/headlines?countryCode={x['Code']}&format=json&language=en-US&apiKey={apiKey}"

            get_detail_key = requests.get(url_weather_headlines)

            if get_detail_key.status_code == 204:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No weather information for this country")

            res = get_detail_key.json()["alerts"][0]["detailKey"]

            url_weatheralert_detail = f"https://api.weather.com/v3/alerts/detail?alertId={res}&format=json&language=en-US&apiKey={apiKey}"
            res = requests.get(url_weatheralert_detail).json()

            countryName = res["alertDetail"]["countryName"]
            countryCode = res["alertDetail"]["countryCode"]
            disclaimer = res["alertDetail"]["disclaimer"]
            endTimeLocal = res["alertDetail"]["endTimeLocal"]
            endTimeLocalTimeZone = res["alertDetail"]["endTimeLocalTimeZone"]
            responseType = res["alertDetail"]["messageType"]
            flood =  res["alertDetail"]["flood"]
            officeName = res["alertDetail"]["officeName"]
            source =res["alertDetail"]["source"]
            longitude = res["alertDetail"]["longitude"]
            latitude = res["alertDetail"]["latitude"]
            headlineText = res["alertDetail"]["headlineText"]
            eventDescription = res["alertDetail"]["eventDescription"]
            severity = res["alertDetail"]["severity"]

            desc = [x["description"] for x in res["alertDetail"]["texts"]]
            return {"countryName": countryName, "countryCode": countryCode, "responseType": responseType, "officeName": officeName, "source": source, "longitude": longitude, "latitude": latitude, "headlineText": headlineText, "eventDescription": eventDescription, "disclaimer": disclaimer, "severity": severity, "flood": flood, "endTimeLocal": endTimeLocal, "endTimeLocalTimeZone": endTimeLocalTimeZone, "description": desc}
