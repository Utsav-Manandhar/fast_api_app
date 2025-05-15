# FastAPI ML Prediction App

This is a web application built using FastAPI that loads a simple machine learning model trained using scikit learn to make predictions based on user input via a form. It returns the probability score calculated by the model.

The project is part of an assignment for the Fusemachines AI Fellowship. The main goal of the project is to build an app using FastAPI while incorporating the 12-Factor App paradigm and following good development practices. 

The app is merely for demonstration purposes and accuracy of results is not guaranteed.


---

##  How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Utsav-Manandhar/fast_api_app.git
cd your-repo
```
### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

###  3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Add Environment Variables

Create a .env file in the root directory and save the following:

MODEL_PATH=models/model.pkl
SCALER_PATH=models/scaler.pkl

### 5. Start the FastAPI Server
```bash
uvicorn main:app --reload
```
Then open your browser and visit:
http://localhost:8000
You should see a form to submit input features.

### Running tests

Make sure you're in the project root and run:

```bash
pytest
```
This will discover and run tests in the tests/ folder.

## Running with Docker (Optional)

## 1.Build the Docker Image
```bash

docker build -t fastapi-ml-app .
```
## 2. Run the Container
```bash

docker run -p 8000:8000 --env-file .env fastapi-ml-app

```
Visit: http://localhost:8000