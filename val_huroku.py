import requests

data = {'age': 33,
        'workclass': 'Private',
        'fnlgt': 149184,
        'education': 'HS-grad',
        'marital_status': 'Never-married',
        'occupation': 'Prof-specialty',
        'relationship': 'Not-in-family',
        'race': 'White',
        'sex': 'Male',
        'hours_per_week': 60,
        'native_country': 'United-States'
                }
r = requests.post('https://mldevopt3.herokuapp.com/', json=data)
assert r.status_code == 200
print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())