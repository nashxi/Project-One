from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers.weather import router as weather_router

app = FastAPI()

app.include_router(weather_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)