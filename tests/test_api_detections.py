def test_api_detection(client):
    response = client.get("/api/v1.0/detection/1")
    assert response.status_code == 200


def test_api_detections(client):
    response = client.get("/api/v1.0/detections/")
    assert response.status_code == 200
