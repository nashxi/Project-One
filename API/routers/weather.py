from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.get_weather_service import get_weather_data

router = APIRouter()


@router.get("/weather")
async def get_weather():
    try:
        weather_data = get_weather_data()
        return JSONResponse(content=weather_data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})