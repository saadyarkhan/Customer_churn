from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.predict import predict_churn
from app.schema import PredictionResponse, CustomerData
import logging
from mangum import Mangum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Customer Churn API")

@app.get("/")
def root():
    return {"message":" Welcome to the Customer Churn API!"}

@app.get("/health")
def health():
    return {"status":"healthy"}


class Customer(BaseModel):
    tenure : float
    monthly_charges : float
    Contract : str

@app.post("/predict", response_model=PredictionResponse)
def predict(customer:CustomerData):
    logger.info(f"Received prediction request for customer: {customer.model_dump()}")
    try:
        prediction, probability = predict_churn(customer.model_dump())
        logger.info(f"Prediction: {prediction}, Probability: {probability}")
        return PredictionResponse(churn_prediction=prediction, churn_probability=probability)
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
        
handler = Mangum(app)