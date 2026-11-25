import pytest
from app import app, init_db, db


@pytest.fixture
def client():
    init_db()
    with db() as conn, conn.cursor() as cur:
        cur.execute("TRUNCATE tasks RESTART IDENTITY")
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.get_json() == {"status": "broken"}
    


def test_list_empty(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == {"tasks": []}


def test_create_task(client):
    r = client.post("/tasks", json={"title": "write tests"})
    assert r.status_code == 201
    body = r.get_json()
    assert body["title"] == "write tests"
    assert body["done"] is False
    assert body["id"] == 1


def test_create_task_missing_title(client):
    r = client.post("/tasks", json={})
    assert r.status_code == 400
    assert "error" in r.get_json()


def test_list_after_create(client):
    client.post("/tasks", json={"title": "a"})
    client.post("/tasks", json={"title": "b"})
    r = client.get("/tasks")
    assert len(r.get_json()["tasks"]) == 2
