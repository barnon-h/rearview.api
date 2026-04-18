from fastapi.testclient import TestClient
from app.main import app

client = TestClient( app )

def test_health():
    response = client.get( "/health" )

    assert response.status_code == 200
    assert response.json() == { "status": "ok" }

def test_predict():
    payload = {
        "year" : 2015,
        "miles" : 50000,
        "make" : "Toyota",
        "model" : "Camry"
    }
    response = client.post( "/predict", json=payload )
    data = response.json()

    assert response.status_code == 200
    assert "predicted_price" in data

    assert isinstance( data[ "predicted_price" ], float )
    assert data[ "predicted_price" ] > 0