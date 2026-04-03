import pytest

def test_health():
    assert True

def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"

class TestProject:
    def test_create(self):
        project = {"title": "Test", "status": "active"}
        assert project["status"] == "active"

    def test_empty_title(self):
        with pytest.raises(ValueError):
            raise ValueError("Title required")