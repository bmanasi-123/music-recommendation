MoodTune (Mood-based Music Recommender)
MoodTune is a FastAPI-based microservice that suggests music based on your mood and local weather. It integrates real-time data from OpenWeatherMap and music recommendations from Last.fm.
________________________________________
📁 Project Versions
This repository contains three different versions of MoodTune to showcase different deployment strategies:
Version	  Description
local-fastapi	  Traditional FastAPI app running locally
aws-lambda	  AWS Lambda-compatible FastAPI app (using Mangum)
aws-lambda-gateway	   Fully serverless setup with Lambda + API Gateway trigger
________________________________________
🧠 Features
•	🎯 Mood + Weather-based music recommendations
•	☁️ Real-time weather from OpenWeatherMap
•	🎶 Music suggestions using Last.fm
•	🧪 Pytest test suite with API and logic testing
•	🔐 Config-based secrets management
•	🛠️ Error handling and logging
•	🌐 Serverless support (Lambda + API Gateway)
________________________________________
🚀 Endpoints Overview
🔍 Explore all endpoints here:
👉 http://localhost:8000/docs (Swagger UI)
🧾 Or view the raw OpenAPI schema:
👉 http://localhost:8000/openapi.json
Endpoint	Method	Description
/	GET	Homepage (if frontend enabled)
/recommend-song	POST	Main endpoint – returns mood-weather matched music
/weather/{city}	GET	Fetch weather by city
/song/{title}	GET	Search a song by title
/song/{mood}	GET	Suggest a song based on mood
________________________________________
⚙️ Config & Secrets
Edit your config file for each version (e.g., config.yaml):
Rename the file as config.yaml from config.yaml.example and update your API keys.
________________________________________
🧪 Running Tests
# Run all tests
Command: “python -m pytest test”

Includes:
•	Unit tests for matcher logic
•	Integration tests for FastAPI endpoints
________________________________________
## 🧪 Postman Collection

You can test the APIs easily using the included Postman collection:

- 📁 **File:** `moodtune.postman_collection.json`
- 🔄 Includes all key endpoints: recommendation, weather, song by title/mood
- 🧑‍💻 Works with the local server (`http://localhost:8000`)

### 🔧 How to Use:

1. Open **Postman**
2. Click **Import**
3. Choose **File** or **Raw Text**
4. Select `moodtune.postman_collection.json` from this repo
5. Run each request and see the response instantly!
________________________________________
☁️ Steps to Run the Application
🖥️ Local FastAPI Version
1.	Unzip the local-fastapi directory.
2.	Install dependencies: “pip install -r requirements.txt”
3.	Update your API keys in config.yaml.
4.	Start the FastAPI server: “python -m uvicorn main:app --reload”
5.	Once the application starts, open your browser and navigate to:
👉 http://localhost:8000
6.	Run test cases: “python -m pytest tests”
________________________________________
⚙️ AWS Lambda Version (Requires AWS Access Key)
1.	Unzip the aws-lambda directory and install dependencies.
2.	Create a new AWS Lambda function, and replace its code with lambda_function.py.
3.	Configure AWS credentials as environment variables:
4.	Follow steps 3–6 from the Local FastAPI Version section above.
________________________________________
🌐 AWS Lambda + API Gateway Version (Recommended)
1.	Unzip the aws-lambda-gateway directory and install dependencies.
2.	Create a new AWS Lambda function, same as AWS Lambda Version
3.	Set up an API Gateway, and link it to the Lambda function.
4.	Obtain the public URL from API Gateway, and add it to your config.yaml if needed.
5.	Follow steps 3–6 from the Local FastAPI Version section above.
________________________________________
🧩 Future Enhancements
•	OAuth-based user preferences
•	Mood classification via AI
•	Spotify integration
________________________________________

