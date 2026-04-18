from fastapi import FastAPI, HTTPException
from app.schema import prediction_request, prediction_response
from app.predictor import predict_price

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI( title = "Rearview.api",
            description= "A simple API to predict car prices based on year, miles, make, and model.")

BASE_DIR = Path(__file__).resolve().parent.parent

app.mount(
    "/static",
    StaticFiles( directory = str(BASE_DIR / "static") ),
    name = "static"
    )

@app.get("/health")
def health() -> dict:
    return { "status": "ok" }

@app.post( "/predict", response_model = prediction_response )
def predict( request : prediction_request ) -> prediction_response:
    try:
        price = predict_price( request.year, request.miles, request.make, request.model )
        return prediction_response( predicted_price = price )
    except Exception as e:
        raise HTTPException( status_code = 400, detail = str( e ))

@app.get( "/" )
def root() -> FileResponse:
    return FileResponse( f"{BASE_DIR}/static/index.html" )