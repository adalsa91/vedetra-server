def test_api_create_and_get_detection(client):
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


def test_api_modify_detection(client):
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

    # Modify md5_mac detections
    detection_json = {
        'md5_mac': '874b165dccb840797ab7decdce8a3a13',
        'timestamp': '1562268716',
        'sensor_id': '3af2733e4aad9fac10547ad6a0d5c318'
    }
    response = client.put(url, json=detection_json)
    assert response.status_code == 200

    # Check modification
    response = client.get(url)
    assert b"874b165dccb840797ab7decdce8a3a13" in response.data


def test_api_delete_detection(client):
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

    # Delete detection
    response = client.delete(url)
    assert response.status_code == 200


def test_api_bulk_insert_detections(client):
    # Write detections
    detections_json = {
      "node": "6e1142a5d86b1eca0ed13b408487fe05",
      "detections": {
        "70fbb859bf3606b8b0b54e30c2f1facd": 1563737210,
        "7598e7b767976cdd583135125da0836f": 1563737209,
        "9331c407b188128654e3c3c218bb10d8": 1563737215
      }
    }

    response = client.post(
        "/api/v1.0/detections-collection/",
        json=detections_json
    )

    assert response.status_code == 201


def test_api_detections(client):
    response = client.get("/api/v1.0/detections/")
    assert response.status_code == 200
