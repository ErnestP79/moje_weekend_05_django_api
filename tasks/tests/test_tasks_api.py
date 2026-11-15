from rest_framework.test import APIClient


def test_tasks_list_returns_200():
    client = APIClient()

    response = client.get("/api/tasks/")

    assert response.status_code == 200
    assert isinstance(response.data, list)


def test_create_task_returns_201():
    client = APIClient()

    payload = {
        "title": "Write API test",
        "description": "Cover POST endpoint",
        "status": "todo",
        "priority": "high",
    }

    response = client.post(
        "/api/tasks/",
        payload,
        format="json"
    )

    assert response.status_code == 201
    assert response.data["title"] == "Write API test"
    assert response.data["status"] == "todo"
    assert response.data["priority"] == "high"


def test_create_task_without_title_returns_400():
    client = APIClient()

    payload = {
        "description": "Missing required title",
        "status": "todo",
        "priority": "medium",
    }

    response = client.post("/api/tasks/", payload, format="json")

    assert response.status_code == 400
    assert "title" in response.data

def test_create_task_with_invalid_status_returns_400():
    client = APIClient()

    payload = {
        "title": "Wrong status",
        "description": "Status is not allowed",
        "status": "blocked",
        "priority": "high",
    }

    response = client.post("/api/tasks/", payload, format="json")

    assert response.status_code == 400
    assert "status" in response.data


def test_create_task_with_invalid_priority_returns_400():
    client = APIClient()

    payload = {
        "title": "Wrong priority",
        "description": "Priority is not allowed",
        "status": "done",
        "priority": "urgent",
    }

    response = client.post("/api/tasks/", payload, format="json")

    assert response.status_code == 400
    assert "priority" in response.data

def test_get_task_details_returns_200():
    client = APIClient()

    response = client.get("/api/tasks/1/")

    assert response.status_code == 200
    assert response.data["id"] == 1
    assert response.data["title"] == "Create Django project"


def test_get_task_details_returns_404():
    client = APIClient()

    response = client.get("/api/tasks/999/")

    assert response.status_code == 404
    assert response.data["error"] == "Task not found"