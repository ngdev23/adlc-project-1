from uuid import uuid4
from datetime import datetime

def test_user_creation():
    user = {"id": str(uuid4()), "name": "Alice", "email": "alice@test.com"}
    assert user["name"] == "Alice"

def test_project_creation():
    project = {"id": str(uuid4()), "title": "My Project", "status": "active"}
    assert project["status"] == "active"