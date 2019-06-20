def test_index(client):
    response = client.get('/')
    assert b"Index" in response.data


def test_detections(client):
    response = client.get('/detections')
    assert b"User ID" in response.data
