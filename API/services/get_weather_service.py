from fastapi import HTTPException
import GetWeather as weather_module


def get_weather_data():
    try:
        weather_data = weather_module.responses
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))