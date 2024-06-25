import requests


df = {"age": 32,
    "workclass": "State-gov",
    "education": "Some-college",
    "maritalStatus": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Female",
    "hoursPerWeek": 40,
    "nativeCountry": "United-States"
    }
r = requests.post('https://censusdata-5416104b4264.herokuapp.com', json=df)
print(r.json())

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())

## Experimental push to check CI