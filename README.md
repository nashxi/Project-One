# Project Title: Weather Fetching Service

## Overview
This project is a FastAPI application that fetches weather data using the Open-Meteo API. It provides endpoints to retrieve current and forecasted weather information based on specified geographical coordinates.

## Project Structure
```
Project-one
├── API
│   ├── GetWeather.py          # Logic to fetch weather data using Open-Meteo API
│   ├── main.py                # Entry point for the FastAPI application
│   ├── routers
│   │   └── weather.py         # FastAPI router for weather-related endpoints
│   ├── services
│   │   └── get_weather_service.py # Service logic for weather data fetching
│   └── requirements.txt       # List of dependencies for the project
├── README.md                  # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd Project-one
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r API/requirements.txt
   ```

## Usage
1. **Run the FastAPI application**:
   ```
   uvicorn API.main:app --reload
   ```

2. **Access the API documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## Endpoints
- **Get Weather**: 
  - **URL**: `/weather`
  - **Method**: `GET`
  - **Query Parameters**:
    - `latitude`: Latitude of the location
    - `longitude`: Longitude of the location
  - **Response**: Returns weather data including temperature, precipitation, and wind speed.

## License
This project is licensed under the MIT License - see the LICENSE file for details.