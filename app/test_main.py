import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app
import mongomock

# Patch Motor's AsyncIOMotorClient to use mongomock
class AsyncIOMotorMockClient:
    def __init__(self, *args, **kwargs):
        self._client = mongomock.MongoClient()
    def get_database(self, name):
        return self._client[name]

# Patch app.state.db for tests
app.state.db = AsyncIOMotorMockClient().get_database("empire_db_test")

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Empire API is Live, Commander."}

def test_signup_and_login():
    # Use a unique email for each test run
    import uuid
    email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"
    signup_data = {
        "name": "Test User",
        "email": email,
        "password": password,
        "age": 30
    }
    # Signup
    response = client.post("/signup", json=signup_data)
    assert response.status_code == 200 or response.status_code == 400
    # Login
    login_data = {"email": email, "password": password}
    response = client.post("/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_users():
    response = client.get("/get_users")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 