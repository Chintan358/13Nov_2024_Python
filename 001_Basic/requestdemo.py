
import requests


data = requests.get("https://restcountries.com/v3.1/all").json()
for i in data:
    print(i['name']['common'])