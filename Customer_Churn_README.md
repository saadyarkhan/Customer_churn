# 🚀 Customer Churn Prediction API

> **Production-ready Machine Learning API** for predicting customer churn using **FastAPI**, **AWS Lambda**, **Docker**, and a fully automated **GitHub Actions CI/CD** pipeline.

---

## ✨ Highlights

- ⚡ FastAPI REST API
- 🤖 Scikit-learn ML Pipeline
- ☁️ AWS Lambda (Serverless)
- 🐳 Docker Containerization
- 🔄 GitHub Actions CI/CD
- 📦 Amazon ECR + S3
- 📚 Interactive Swagger Docs
- ✅ Automated Testing with pytest

---

## 🌐 Live Demo

| Resource | Link |
|----------|------|
| API | https://gg871moh5j.execute-api.us-east-1.amazonaws.com |
| Swagger Docs | https://gg871moh5j.execute-api.us-east-1.amazonaws.com/docs |

---

# 📖 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project predicts whether a customer is likely to churn and exposes the trained model through a scalable REST API.

Unlike notebook-only ML projects, this repository demonstrates the **complete production lifecycle**:

```text
Data → Model Training → FastAPI → Docker → AWS Lambda
          ↓
 GitHub Actions CI/CD → Amazon ECR → API Gateway
```

---

# 🏗️ Architecture

```text
                Client
                   │
                   ▼
            API Gateway
                   │
                   ▼
             AWS Lambda
                   │
                   ▼
             FastAPI App
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
  ML Pipeline           Health Check
         │
         ▼
     Prediction
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| ML | pandas, scikit-learn |
| API | FastAPI, Pydantic |
| Cloud | AWS Lambda, API Gateway, S3, ECR |
| DevOps | Docker, GitHub Actions |
| Testing | pytest, httpx |

---

# ⭐ Features

- REST API with validation
- Interactive Swagger documentation
- Structured logging
- Centralized error handling
- Automated CI/CD
- Dockerized deployment
- Serverless architecture
- Unit testing

---

# 📊 Model Summary

**Dataset**

- Telco Customer Churn
- ~7,000 customers

**Target**

- Churn (Yes / No)

**Pipeline**

- One-Hot Encoding
- Feature Scaling
- ColumnTransformer
- Scikit-learn Pipeline

---

# 📈 Why This Project?

✅ Demonstrates production ML deployment

✅ Cloud-native architecture

✅ Serverless inference

✅ API development

✅ CI/CD automation

✅ Containerization

---

# 📂 Project Structure

```text
app/
models/
tests/
src/
.github/workflows/
Dockerfile
Dockerfile.lambda
requirements.txt
README.md
```

---

# 🚀 CI/CD Workflow

```text
Developer Push
      │
      ▼
GitHub Actions
      │
      ▼
Run Tests
      │
      ▼
Build Docker Image
      │
      ▼
Push to Amazon ECR
      │
      ▼
Deploy AWS Lambda
      │
      ▼
API Live 🎉
```

---

# 🔮 Future Roadmap

- Model Monitoring
- Authentication
- MLflow Integration
- Drift Detection
- Model Registry
- CloudWatch Dashboard

---

# 👨‍💻 Skills Demonstrated

Python • FastAPI • Scikit-learn • Docker • AWS Lambda • API Gateway • Amazon ECR • Amazon S3 • GitHub Actions • CI/CD • REST APIs • Serverless • Machine Learning • Testing

---


