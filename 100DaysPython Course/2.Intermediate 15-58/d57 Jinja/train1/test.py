import requests


genderizer_url = 'https://api.genderize.io'
age_url = 'https://api.agify.io'

param = {
    'name': 'ruben'
}

response = requests.get(url=genderizer_url, params=param)
gender = response.json()

response= requests.get(url=age_url, params=param)
age = response.json()



print(gender['gender'])
print(age['age'])
