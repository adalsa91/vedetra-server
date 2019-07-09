def test_api_detection(client):

    # Write a detection
    detection_json = {
        'md5_mac': '874b165dccb840797ab7decdce8a3a40',
        'timestamp': '1562268716',
        'sensor_id': '3af2733e4aad9fac10547ad6a0d5c318'
    }

    response = client.post(
        "/api/v1.0/detections/",
        json=detection_json
    )

    assert response.status_code == 201
    url = response.headers.get('Location')
    assert url is not None

    # Get the new detection
    response = client.get(url)
    assert response.status_code == 200


def test_api_detections(client):
    response = client.get("/api/v1.0/detections/")
    assert response.status_code == 200
