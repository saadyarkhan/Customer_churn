import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "my_model.pkl"
print("Looking for model at:", MODEL_PATH)
print("Exists?", MODEL_PATH.exists())

model = joblib.load(MODEL_PATH)
def predict_churn(customer_dict: dict):
    input_df = pd.DataFrame([customer_dict])
    prediction = model.predict(input_df)[0]              
    probability = model.predict_proba(input_df)[:, 1][0]  
    return int(prediction), float(probability)
