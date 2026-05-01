from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib, json, numpy as np
from sklearn.preprocessing import LabelEncoder

app = FastAPI(title="Churn Prediction API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models & meta
model_rf = joblib.load("model_rf.pkl")
model_gb = joblib.load("model_gb.pkl")
model_lr = joblib.load("model_lr.pkl")
scaler   = joblib.load("scaler.pkl")

with open("model_meta.json") as f:
    meta = json.load(f)

MODELS = {
    "Random Forest":       model_rf,
    "Gradient Boosting":   model_gb,
    "Logistic Regression": model_lr,
}

class CustomerInput(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    model: str = "Random Forest"

def encode_input(data: CustomerInput):
    le = LabelEncoder()
    row = {
        'tenure': data.tenure,
        'MonthlyCharges': data.MonthlyCharges,
        'TotalCharges': data.TotalCharges,
        'gender': data.gender,
        'SeniorCitizen': data.SeniorCitizen,
        'Partner': data.Partner,
        'Dependents': data.Dependents,
        'PhoneService': data.PhoneService,
        'MultipleLines': data.MultipleLines,
        'InternetService': data.InternetService,
        'OnlineSecurity': data.OnlineSecurity,
        'TechSupport': data.TechSupport,
        'Contract': data.Contract,
        'PaperlessBilling': data.PaperlessBilling,
        'PaymentMethod': data.PaymentMethod,
    }

    cat_cols = meta['cat_cols']
    encoders = meta['encoders']

    for col in cat_cols:
        options = encoders[col]
        val = row[col]
        if val not in options:
            raise ValueError(f"Invalid value '{val}' for '{col}'")
        le.fit(options)
        row[col] = int(le.transform([val])[0])

    features = meta['features']
    X = np.array([[row[f] for f in features]])
    return X

@app.get("/")
def root():
    return {"message": "Churn Prediction API is running", "models": list(MODELS.keys())}

@app.get("/accuracies")
def get_accuracies():
    return meta['accuracies']

@app.get("/options")
def get_options():
    return meta['encoders']

@app.post("/predict")
def predict(customer: CustomerInput):
    if customer.model not in MODELS:
        raise HTTPException(status_code=400, detail=f"Model must be one of: {list(MODELS.keys())}")

    try:
        X = encode_input(customer)
        X_scaled = scaler.transform(X)
        model = MODELS[customer.model]
        prediction = int(model.predict(X_scaled)[0])
        proba = model.predict_proba(X_scaled)[0]
        churn_prob = float(proba[1])

        if churn_prob >= 0.7:
            risk = "High Risk"
        elif churn_prob >= 0.4:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"

        return {
            "churn": bool(prediction),
            "churn_probability": round(churn_prob * 100, 2),
            "risk_level": risk,
            "model_used": customer.model,
            "model_accuracy": round(meta['accuracies'][customer.model] * 100, 2),
        }
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/predict/batch")
def predict_batch(customers: list[CustomerInput]):
    results = []
    for c in customers:
        try:
            r = predict(c)
            results.append({"status": "success", **r})
        except Exception as e:
            results.append({"status": "error", "detail": str(e)})
    return results
