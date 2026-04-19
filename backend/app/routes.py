# routes.py
# All API endpoints live here
# Frontend (React) calls these endpoints to get data

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api")


# ─────────────────────────────────────────
# BASIC ENDPOINTS
# ─────────────────────────────────────────

# GET /api/hello
@router.get("/hello")
def hello():
    return {
        "message": "Hello from FastAPI Backend!",
        "status": "connected"
    }


# GET /api/pipeline-info
@router.get("/pipeline-info")
def pipeline_info():
    return {
        "pipeline": "GitHub Actions",
        "stages": [
            "Code Push",
            "Checkout",
            "Build Frontend",
            "Build Backend",
            "Run Tests",
            "Docker Build",
            "Docker Deploy"
        ],
        "status": "All stages passed"
    }


# ─────────────────────────────────────────
# DATA ENDPOINT
# ─────────────────────────────────────────

class DataInput(BaseModel):
    name: str
    value: str

# POST /api/data
@router.post("/data")
def process_data(input: DataInput):
    return {
        "received": {
            "name": input.name,
            "value": input.value
        },
        "processed": f"Backend processed: {input.name} = {input.value}",
        "status": "success"
    }


# ─────────────────────────────────────────
# AI READY ENDPOINT
# ─────────────────────────────────────────

# POST /api/predict
# Ready for your AI model later
@router.post("/predict")
def predict(input: DataInput):
    return {
        "input": input.value,
        "prediction": "AI model not loaded yet",
        "note": "Replace this with your actual ML model",
        "status": "placeholder"
    }