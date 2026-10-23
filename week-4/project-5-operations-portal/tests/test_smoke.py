from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_feature_is_unimplemented():
    assert client.get("/portal").status_code == 501
# TODO: Replace the 501 expectation with real behavior tests.
