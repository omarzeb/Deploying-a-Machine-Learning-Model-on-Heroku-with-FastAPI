def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Welcome to the FAST API Inference!"}


def test_post_right(client):
    request = client.post("/", json={'age': 19,
                                     'workclass': 'Private',
                                     'fnlgt': 149184,
                                     'education': 'HS-grad',
                                     'marital_status': 'Never-married',
                                     'occupation': 'Prof-specialty',
                                     'relationship': 'Not-in-family',
                                     'race': 'White',
                                     'sex': 'Male',
                                     'hoursPerWeek': 60,
                                     'nativeCountry': 'United-States'
                                     })
    assert request.status_code == 200


def test_post_wronge(client):
    request = client.post("/", json={'age': 19,
                                     'workclass': 'Private',
                                     'fnlgt': "This should be int",
                                     'education': 'HS-grad',
                                     'marital_status': 'Never-married',
                                     'occupation': 'Prof-specialty',
                                     'relationship': 'Not-in-family',
                                     'race': 'White',
                                     'sex': 'Male',
                                     'hoursPerWeek': 60,
                                     'nativeCountry': 'United-States'
                                     })
    assert request.status_code == 422

