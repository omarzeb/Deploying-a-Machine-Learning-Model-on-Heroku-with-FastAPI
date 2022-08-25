def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Welcome to the FAST API Inference!"}


def test_post_right(client):
    request = client.post("/", json={'age': 33,
                                     'workclass': 'Private',
                                     'fnlgt': 149184,
                                     'education': 'HS-grad',
                                     'marital-status': 'Never-married',
                                     'occupation': 'Prof-specialty',
                                     'relationship': 'Not-in-family',
                                     'race': 'White',
                                     'sex': 'Male',
                                     'hours-per-week': 60,
                                     'native-country': 'United-States'
                })

    print(request.json())
    assert request.status_code == 200


def test_post_wronge(client):
    request = client.post("/", json={'age': 19,
                 'workclass': 'Private',
                 'fnlgt': "This should be int",
                 'education': 'HS-grad',
                 'marital_status': 'Never-married',
                 'occupation': 'Own-child',
                 'relationship': 'Husband',
                 'race': 'Black',
                 'sex': 'Male',
                 'hours_per_week': 40,
                 'native_country': 'United-States'
                })
    assert request.status_code == 422

