from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.cancer import CancerPredictIn
import joblib


router = APIRouter()

model = joblib.load("cancer_model.joblib")


@router.post("/predict")
def predict(cancer: CancerPredictIn):
    result = model.predict([[cancer.radius_mean, cancer.texture_mean]])
    return JSONResponse({"result": result[0]})
