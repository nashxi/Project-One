from fastapi import FastAPI
from routers.weather import router as weather_router

app = FastAPI()

app.include_router(weather_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather API"}