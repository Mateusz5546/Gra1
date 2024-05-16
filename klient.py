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
    url = "http://127.0.0.1:8000"
    res = requests.get(url + f"/build_structure/{kraj_id}/{budynek_id}")
    data = res.json()
    print(data)
def print_dodane_surowce(kraj_id):
    url = "http://127.0.0.1:8000"
    res = requests.get(url + f"/add_resorces/{kraj_id}")
    data = res.json()
    print("Dodane surowce")
    drewno = data['drewno']
    stal = data['stal']
    jedzenie = data['jedzenie']
    print(drewno,stal,jedzenie)

print_kraje()
id_wybrane = int(input("Wybierz kraj"))
print_resorces(id_wybrane)

sprawdz_kraj(id_wybrane)

print_builds()
budynek_id = int(input("Wybierz co chcesz zbudować: "))
build(id_wybrane,budynek_id)
print_resorces(id_wybrane)

print_dodane_surowce(id_wybrane)



