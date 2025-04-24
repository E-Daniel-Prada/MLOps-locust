from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Métricas Prometheus
REQUEST_COUNT = Counter('predict_requests_total', 'Total de peticiones de predicción')
REQUEST_LATENCY = Histogram('predict_latency_seconds', 'Tiempo de latencia de predicción')

# Definimos la estructura esperada del JSON de entrada
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: InputData) -> Any:
    # Simulación de inferencia: aca se debe reemplazar esta lógica por una real
    dummy_result = data.feature1 + data.feature2 + data.feature3  # solo suma

    return {
        "message": "Predicción generada exitosamente",
        "input": data.dict(),
        "resultado": dummy_result  # valor simulado
    }
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

