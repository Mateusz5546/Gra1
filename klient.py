import requests


url = "http://127.0.0.1:8000"

def print_resorces(id_wybrane):
    url = "http://127.0.0.1:8000"
    res2 = requests.get(url + f"/country/{id_wybrane}")
    data2 = res2.json()
    print(data2[2:])
def sprawdz_kraj(id_wybrane):
    url = "http://127.0.0.1:8000"
    res = requests.get(url + "/countries")
    data = res.json()
    for id, nazwa, drewno, stal, jedzenie in data:
        if id == id_wybrane:
            break
    print(id, nazwa, drewno, stal, jedzenie)
def print_kraje():
    url = "http://127.0.0.1:8000"
    res = requests.get(url + "/countries")
    data = res.json()
    for id, nazwa, _, _, _ in data:
        print(id, nazwa)
def print_builds():
    url = "http://127.0.0.1:8000"
    res = requests.get(url + "/structures")
    data = res.json()
    for id,nazwa,_,_,_ in data:
        print(id,nazwa)

def build(kraj_id,budynek_id):
    input("Co chcesz zbudowac")
    url = "http://127.0.0.1:8000"
    res = requests.get(url + f"/build_structure/{kraj_id}/{budynek_id}")
    data = res.json()
print_kraje()
id_wybrane = int(input("Wybierz kraj"))
print_resorces(id_wybrane)
sprawdz_kraj(id_wybrane)
print_builds()




