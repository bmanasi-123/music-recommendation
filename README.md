# 🎵 **MoodTune** – *Mood-Based Music Recommender*

**MoodTune** is a FastAPI-based microservice that suggests music based on your **mood** and **local weather**. It integrates real-time data from **OpenWeatherMap** and music recommendations from **Last.fm**.

---

## 📁 Project Versions

This repository includes **three deployment-ready versions** to showcase different deployment strategies:

| Version               | Description                                              |
|-----------------------|----------------------------------------------------------|
| `local-fastapi`       | Traditional FastAPI app running locally                  |
| `aws-lambda`          | AWS Lambda-compatible FastAPI app using **Mangum**       |
| `aws-lambda-gateway`  | Fully serverless setup with Lambda + API Gateway trigger |

---

## 🧠 Features

- 🎯 Mood + Weather-based music recommendations  
- ☁️ Real-time weather from **OpenWeatherMap**  
- 🎶 Music suggestions using **Last.fm**  
- 🧪 Full Pytest suite for logic & API testing  
- 🔐 Secrets managed via config file  
- 🛠️ Robust error handling & logging  
- 🌐 Serverless-ready (AWS Lambda + API Gateway)

---

## 🚀 Endpoints Overview

📘 **Swagger UI**: [`http://localhost:8000/docs`](http://localhost:8000/docs)  
📄 **OpenAPI Schema**: [`http://localhost:8000/openapi.json`](http://localhost:8000/openapi.json)

| Endpoint                  | Method | Description                                   |
|---------------------------|--------|-----------------------------------------------|
| `/`                       | GET    | Homepage (if frontend enabled)                |
| `/recommend-song`         | POST   | Main endpoint – returns mood-weather music    |
| `/weather/{city}`         | GET    | Fetch real-time weather by city               |
| `/song/{title}`           | GET    | Search song by title                          |
| `/song/{mood}`            | GET    | Suggest song based on mood                    |

---

## 🔐 Config & Secrets

1. Copy `config.yaml.example` to `config.yaml`
2. Add your **API keys** from:
   - [OpenWeatherMap](https://openweathermap.org/)
   - [Last.fm](https://www.last.fm/api)

---

## 🧪 Running Tests

Run the full test suite:

```bash
python -m pytest tests
```

Test Coverage:

- ✅ Unit tests for mood-weather matching logic  
- ✅ Integration tests for all FastAPI endpoints  

---

## 🔧 Postman Collection

Easily test the API using Postman.

- 📂 **File:** `moodtune.postman_collection.json`
- 🔄 Includes all major endpoints

### How to Use:

1. Open **Postman**
2. Click **Import**
3. Select the file: `moodtune.postman_collection.json`
4. Run any request against `http://localhost:8000`

---

## ☁️ Run the Application

### 🖥️ Local FastAPI Version

```bash
# 1. Navigate to local-fastapi directory
cd local-fastapi

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add API keys to config.yaml

# 4. Start FastAPI server
uvicorn main:app --reload

# 5. Access it via browser
http://localhost:8000

# 6. Run test cases
python -m pytest tests
```

---

### ⚙️ AWS Lambda Version (via Mangum)

```bash
# 1. Navigate to aws-lambda directory
cd aws-lambda

# 2. Install dependencies (in Lambda layer or zip it with venv)

# 3. Replace AWS Lambda function code with `lambda_function.py`

# 4. Configure AWS credentials and environment variables
# 5. Add config.yaml as needed
```

---

### 🌐 AWS Lambda + API Gateway (Fully Serverless)

```bash
# 1. Navigate to aws-lambda-gateway
cd aws-lambda-gateway

# 2. Install dependencies

# 3. Deploy function to AWS Lambda

# 4. Connect to API Gateway → Generate public URL

# 5. Add API Gateway URL to config.yaml if needed

# 6. Deploy and test
```

---

## 🔮 Future Enhancements

- 🔑 OAuth-based user preference profiles  
- 🧠 AI-based mood classification from text/image  
- 🎧 Spotify API integration for richer recommendations  

---
