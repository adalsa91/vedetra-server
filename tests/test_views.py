def test_index(client):
    response = client.get('/')
    assert b"detections" in response.data


def test_detections_view(client):
    response = client.get('/detections')
    assert b"User ID" in response.data


def test_sensors_view(client):
    response = client.get('/detections')
    assert b"Sensor ID" in response.data
