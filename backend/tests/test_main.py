# test_main.py
# Automated tests for your FastAPI backend
# GitHub Actions runs these automatically
# If any test fails → pipeline STOPS

from fastapi.testclient import TestClient
import sys
import os

# Adds backend folder to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)


# TEST 1: Health Check
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    print("✅ Health check passed")


# TEST 2: Hello Endpoint
def test_hello():
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert "message" in response.json()
    print("✅ Hello endpoint passed")


# TEST 3: Pipeline Info Endpoint
def test_pipeline_info():
    response = client.get("/api/pipeline-info")
    assert response.status_code == 200
    assert "stages" in response.json()
    print("✅ Pipeline info endpoint passed")


# TEST 4: Data Processing Endpoint
def test_process_data():
    response = client.post("/api/data", json={
        "name": "test",
        "value": "hello"
    })
    assert response.status_code == 200
    assert "processed" in response.json()
    print("✅ Data processing endpoint passed")