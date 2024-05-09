import requests

url = "http://127.0.0.1:8000"

res = requests.get(url+"/countries")
data = res.json()
for id,nazwa,_,_,_ in data:
    print(id,nazwa)
id_wybrane = int(input("Wybierz kraj"))


for id,nazwa,drewno,stal,jedzenie in data:
    if id == id_wybrane:
        break
print(id,nazwa,drewno,stal,jedzenie)