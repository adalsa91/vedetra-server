def test_api_create_and_get_sensor(client):
    # Write a sensor
    sensor_json = {
        'id': '3af2733e4aad9fac10547ad6a0d5c318',
        'description': 'Sensor 1'
    }

    response = client.post(
        "/api/v1.0/sensors/",
        json=sensor_json
    )

    assert response.status_code == 201
    url = response.headers.get('Location')
    assert url is not None

    # Get the new detection
    response = client.get(url)
    assert response.status_code == 200


def test_api_modify_sensor(client):
    # Write a sensor
    sensor_json = {
        'id': '3af2733e4aad9fac10547ad6a0d5c318',
        'description': 'Sensor 1'
    }

    response = client.post("/api/v1.0/sensors/", json=sensor_json)
    assert response.status_code == 201
    url = response.headers.get('Location')
    assert url is not None

    # Modify description of sensor
    sensor_json = {
        'description': 'Nuevo nombre'
    }

    response = client.put(url, json=sensor_json)
    assert response.status_code == 200

    # Check modification
    response = client.get(url)
    assert b"Nuevo nombre" in response.data


def test_api_delete_sensor(client):
    # Write a sensor
    sensor_json = {
        'id': '3af2733e4aad9fac10547ad6a0d5c318',
        'description': 'Sensor 1'
    }

    response = client.post("/api/v1.0/sensors/", json=sensor_json)

    assert response.status_code == 201
    url = response.headers.get('Location')
    assert url is not None

    # Delete sensor
    response = client.delete(url)
    assert response.status_code == 200


def test_api_get_sensors(client):
    response = client.get("/api/v1.0/sensors/")
    assert response.status_code == 200
