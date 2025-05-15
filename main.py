from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import numpy as np
import joblib
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def make_prediction(features):

    input_data = np.array(features).reshape(1, -1)
    
    MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")
    SCALER_PATH = os.getenv("SCALER_PATH", "models/scaler.pkl")
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict_proba(input_data_scaled)
    perc = prediction*100
    return perc[0,0]
    

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    

@app.post("/submit")
async def submit_form(
    request: Request,
    name: str = Form(...),
    radius: float = Form(...),
    texture: float = Form(...),
    perimeter: float = Form(...),
    area: float = Form(...),
    smoothness: float = Form(...),
    compactness: float = Form(...),
    concavity: float = Form(...),
    concavePoints: float = Form(...),
    symmetry: float = Form(...),
    fractalDimension: float = Form(...)
):
    features = [
        radius, texture, perimeter, area,
        smoothness, compactness, concavity,
        concavePoints, symmetry, fractalDimension
    ]
    percent = make_prediction(features)

          
    return templates.TemplateResponse("result.html", {
        "request": request,
        "name": name,
        "percent": round(percent, 2)
    })