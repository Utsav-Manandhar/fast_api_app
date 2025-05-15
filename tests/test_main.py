from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "html" in response.headers["content-type"].lower()

def test_submit_route():
    form_data = {
        "name": "Test User",
        "radius": 10.0,
        "texture": 15.0,
        "perimeter": 70.0,
        "area": 500.0,
        "smoothness": 0.1,
        "compactness": 0.2,
        "concavity": 0.3,
        "concavePoints": 0.2,
        "symmetry": 0.15,
        "fractalDimension": 0.05
    }

    response = client.post("/submit", data=form_data)
    assert response.status_code == 200
    assert "html" in response.headers["content-type"].lower()
    assert "Test User" in response.text
