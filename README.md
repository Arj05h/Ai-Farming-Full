# AI Farming Full Project

AI Farming Full is a full-stack starter that combines a FastAPI backend with a modern
single-page control center for monitoring farms, managing recommendations, and forecasting
crop yields.

## Features

- **Sensor overview** for soil moisture and temperature.
- **Recommendation feed** with prioritized farm actions.
- **Yield forecasting** endpoint with confidence scores.
- **Responsive UI** for field dashboards and action queues.

## Project structure

```
backend/
  app/
    main.py
  requirements.txt
frontend/
  app.js
  index.html
  styles.css
```

## Backend setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Frontend setup

Open `frontend/index.html` in your browser, or serve it with a local static server.

## Sample API requests

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/sensors
curl http://127.0.0.1:8000/recommendations
curl -X POST http://127.0.0.1:8000/forecast \
  -H 'Content-Type: application/json' \
  -d '{"crop":"Maize","area_hectares":25,"soil_moisture":32,"expected_rain_mm":18}'
```
