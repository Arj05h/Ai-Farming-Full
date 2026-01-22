from datetime import date
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Farming Platform", version="1.0.0")


class SensorReading(BaseModel):
    sensor_id: str
    label: str
    value: float
    unit: str
    captured_on: date


class Recommendation(BaseModel):
    title: str
    details: str
    priority: str


class ForecastRequest(BaseModel):
    crop: str
    area_hectares: float
    soil_moisture: float
    expected_rain_mm: float


class ForecastResponse(BaseModel):
    crop: str
    yield_estimate_tons: float
    confidence: float
    notes: List[str]


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok", "service": "ai-farming"}


@app.get("/sensors", response_model=List[SensorReading])
async def list_sensor_readings() -> List[SensorReading]:
    today = date.today()
    return [
        SensorReading(
            sensor_id="soil-01",
            label="Soil Moisture",
            value=32.4,
            unit="%",
            captured_on=today,
        ),
        SensorReading(
            sensor_id="temp-02",
            label="Ambient Temp",
            value=26.1,
            unit="°C",
            captured_on=today,
        ),
    ]


@app.get("/recommendations", response_model=List[Recommendation])
async def get_recommendations() -> List[Recommendation]:
    return [
        Recommendation(
            title="Increase irrigation block A",
            details="Moisture is below target by 8%. Schedule a 30-minute drip cycle.",
            priority="high",
        ),
        Recommendation(
            title="Nitrogen boost",
            details="Apply 12 kg/ha urea within 48 hours to support maize growth.",
            priority="medium",
        ),
    ]


@app.post("/forecast", response_model=ForecastResponse)
async def forecast_yield(payload: ForecastRequest) -> ForecastResponse:
    estimated_yield = payload.area_hectares * (payload.soil_moisture / 100) * 4.5
    confidence = min(0.95, 0.55 + (payload.expected_rain_mm / 200))
    notes = [
        "Forecast assumes stable temperature range.",
        "Review irrigation schedule if rainfall shifts >20mm.",
    ]
    return ForecastResponse(
        crop=payload.crop,
        yield_estimate_tons=round(estimated_yield, 2),
        confidence=round(confidence, 2),
        notes=notes,
    )
