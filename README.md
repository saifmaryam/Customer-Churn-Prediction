<div align="center">

# 🔮 ChurnSense AI
### Customer Churn Prediction System

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Railway](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Frontend-GitHub_Pages-222222?style=for-the-badge&logo=github&logoColor=white)

<br/>

> **Predict which telecom customers are about to leave — before they do.**  
> Powered by 3 ML models, a REST API, and a sleek dark-themed dashboard.

<br/>

---

</div>

## 📸 Preview

```
┌─────────────────────────────────────────────────────┐
│  🔮 ChurnSense          RF: 90.3%  GB: 91.8%  LR: 78%  │
├──────────────────────────┬──────────────────────────┤
│   📋 Customer Profile    │   📊 Prediction Result   │
│                          │                          │
│  Tenure: [12 months]     │  🔴 HIGH RISK            │
│  Monthly: [$65.50]       │  Likely to Churn         │
│  Contract: [M-to-M]      │                          │
│  Internet: [Fiber]       │  Churn Probability       │
│  ...                     │  ████████░░  74.3%       │
│                          │                          │
│  [🌲 RF] [⚡ GB] [📈 LR] │  Model: Random Forest    │
│                          │  Accuracy: 90.35%        │
│  [ 🔍 ANALYZE CHURN ]    │                          │
└──────────────────────────┴──────────────────────────┘
```

---

## ✨ Features

- 🤖 **3 ML Models** — Random Forest, Gradient Boosting, Logistic Regression
- 📊 **Real-time Prediction** — Churn probability with risk level (High / Medium / Low)
- 🎨 **Stunning Dark UI** — Animated dashboard, no frameworks needed
- ⚡ **FastAPI Backend** — Auto-generated `/docs` (Swagger UI)
- 📦 **Batch Predictions** — Multiple customers at once via API
- 🌐 **CORS Ready** — Connect any frontend instantly

---

## 🧠 Model Performance

| Model | Accuracy | Best For |
|---|---|---|
| 🌲 Random Forest | **90.3%** | Balanced performance |
| ⚡ Gradient Boosting | **91.8%** | Highest accuracy |
| 📈 Logistic Regression | **78.1%** | Fast & interpretable |

> Models trained on **7,043 telecom customers** with 15 features including tenure, contract type, internet service, monthly charges, and more.

---

## 📁 Project Structure

```
churn-prediction/
│
├── 📂 backend/
│   ├── main.py              # FastAPI app — all endpoints
│   ├── requirements.txt     # Python dependencies
│   ├── nixpacks.toml        # Railway deployment config
│   ├── model_rf.pkl         # Trained Random Forest
│   ├── model_gb.pkl         # Trained Gradient Boosting
│   ├── model_lr.pkl         # Trained Logistic Regression
│   ├── scaler.pkl           # Feature scaler
│   └── model_meta.json      # Feature encodings & accuracy scores
│
├── 📂 frontend/
│   └── index.html           # Complete UI (HTML + CSS + JS)
│
└── README.md
```

---

## 🚀 Run Locally

### Step 1 — Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/churn-prediction.git
cd churn-prediction
```

### Step 2 — Start the Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

✅ API running at: `http://localhost:8000`  
📖 Swagger Docs at: `http://localhost:8000/docs`

### Step 3 — Open the Frontend
```bash
# Option 1: Just open in browser
open frontend/index.html

# Option 2: Use VS Code Live Server extension
# Right-click index.html → "Open with Live Server"
```

> ⚠️ Make sure backend is running before opening the frontend.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/accuracies` | All model accuracy scores |
| `GET` | `/options` | Valid values for each field |
| `POST` | `/predict` | Predict single customer |
| `POST` | `/predict/batch` | Predict multiple customers |

### 📤 Request Example
```json
POST /predict
{
  "tenure": 12,
  "MonthlyCharges": 65.5,
  "TotalCharges": 786.0,
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "TechSupport": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "model": "Random Forest"
}
```

### 📥 Response Example
```json
{
  "churn": true,
  "churn_probability": 74.32,
  "risk_level": "High Risk",
  "model_used": "Random Forest",
  "model_accuracy": 90.35
}
```

---

## ☁️ Deployment Guide

### Frontend → GitHub Pages (FREE)
1. Push code to GitHub
2. Go to repo **Settings → Pages**
3. Source: `main` branch → `/frontend` folder
4. Save → Your frontend is live! 🎉

### Backend → Railway.app (FREE)
1. Go to [railway.app](https://railway.app) → New Project
2. Deploy from GitHub repo
3. Set **Root Directory** → `backend`
4. Set **Start Command** → `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Deploy → Copy your Railway URL

### 🔗 Connect Frontend to Live Backend
After Railway gives you a URL, edit one line in `frontend/index.html`:
```javascript
// Change this:
const API = 'http://localhost:8000';

// To your Railway URL:
const API = 'https://your-app-name.railway.app';
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **ML Models** | Scikit-learn (RF, GBM, LR) |
| **API** | FastAPI + Uvicorn |
| **Data Processing** | Pandas, NumPy, Joblib |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Backend Hosting** | Railway.app |
| **Frontend Hosting** | GitHub Pages |

---

## 👤 Author

**Saif / Maryam**  
🔗 GitHub: [@saifmaryam](https://github.com/saifmaryam)

---

<div align="center">

Made with ❤️ — **ChurnSense AI**

⭐ Star this repo if you found it helpful!

</div>
