import requests

url = "http://127.0.0.1:8000"

res = requests.get(url+"/countries")
data = res.json()
for country in data:
    print(country)