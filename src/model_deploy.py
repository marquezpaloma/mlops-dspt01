from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Cargar modelo
from pathlib import Path
import joblib
BASE_DIR = Path(__file__).resolve().parents[1]
model = joblib.load(BASE_DIR / "models" / "model.pkl")

# Esquema de entrada
class InputData(BaseModel):
    data: list [float]

@app.get("/")
def read_root():
    return {"message": "API del modelo funcionando"}

@app.post("/predict")
def predict(input_data: InputData):

    df = pd.DataFrame([input_data.data])

    # usar nombres reales del modelo
    df.columns = model.feature_names_in_

    pred = model.predict(df)

    return {"prediction": pred.tolist()}

print("Features del modelo:", model.feature_names_in_)
print("Cantidad:", len(model.feature_names_in_))