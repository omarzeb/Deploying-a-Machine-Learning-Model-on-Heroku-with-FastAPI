import requests

data = {'age': 19,
                 'workclass': 'Private',
                 'fnlgt': 77516,
                 'education': 'HS-grad',
                 'marital-status': 'Never-married',
                 'occupation': 'Own-child',
                 'relationship': 'Husband',
                 'race': 'Black',
                 'sex': 'Male',
                 'hours-per-week': 40,
                 'native-country': 'United-States'
                 }

r = requests.post('https://mldevopt3.herokuapp.com/', json=data)
print(r)
assert r.status_code == 200
