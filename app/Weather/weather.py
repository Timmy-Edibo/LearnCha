from operator import or_
from fastapi import Depends, APIRouter, HTTPException, status, File, UploadFile, Form, Body
from sqlalchemy.orm import Session

from .. import  models
from ..Weather import weather_rain, weather_detail, weather_forecast, weather_now
from ..Weather.weather_forecast import weatherForecast, weatherForecastGeoCode

from app.database import SessionLocal, engine

router = APIRouter(tags=['Weather'])
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/weather_info")
async def weather_info(country: str = Form()):
    """_summary_

    country: US, Canada, Japan, Western Europe, Australia, spain, Portuges or any country

    204 Error Signifies that they are no weather information vailable for that country
    """

    return weather_detail.weatherDetail(country_=country)

@router.post("/forecast_weather")
def weather_forecast(location: str = Form()):
    """_summary_

    To get accurate weather forecast, Enter input in this format:\n
   current location, state/province, country
    """
    return weatherForecast(location)


@router.post("/forecast_weather/geo_code")
def weather_forecast_geocode(long: str = Form(), latt: str = Form()):
    """_summary_

    To get accurate weather forecast, Enter input in this format:\n
   longitude and latitude
    """
    return weatherForecastGeoCode(long=long, latt=latt)



@router.post("/predict_rainfall")
def weather_forecast(location: str = Form()):
    """_summary_

   To get accurate weather forecast, Enter input in this format:\n
   current location, state/province, country

    """
    return weather_rain.checkRainFall(location.lower())


@router.post("/predict_current_weather")
def weather_current(country: str = Form()):
    """_summary_

   TO get accurate weather forecast, Enter input in this format:\n
   current location, state/province, country

    """
    return weather_now.checkCurrentWeather(country.lower())