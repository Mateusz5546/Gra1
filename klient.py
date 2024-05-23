import requests


url = "http://127.0.0.1:8000"

def print_resources(id_wybrane):
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
            print("Kraj został wybrany pomyślnie")
            break
    print(id, nazwa, drewno, stal, jedzenie)
def sprawdz_kraj():
    url = "http://127.0.0.1:8000"
    res = requests.get(url + "/countries")
    data = res.json()
    for id, nazwa, _, _, _ in data:
        print(id, nazwa)
    id_wybrane = int(input("Wybierz kraj: "))
    while id_wybrane not in [country[0] for country in data]:
        print("To nie jest poprawny numer kraju")
        id_wybrane = int(input("Wybierz kraj: "))
    return id_wybrane
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

def recruit(kraj_id,liczba_jednostek):
    url = "http://127.0.0.1:8000"
    res = requests.get(url + f"/recruit_army/{kraj_id}/{liczba_jednostek}")
    data = res.json()
    print("Zostały zużyte surowce: ",data['resources'])

def select_units(kraj_id):
    url = "http://127.0.0.1:8000"
    res = requests.get(url + f"/country/{kraj_id}")
    data = res.json()
    num_units = data[1]  # Assuming that units are in the second position of the response
    selected_units = int(input(f"Enter the number of units you want to use for the attack (max {num_units}): "))
    while selected_units > num_units:
        print("Invalid number of units selected.")
        selected_units = int(input(f"Enter the number of units you want to use for the attack (max {num_units}): "))
    return selected_units

def attack_opponent(attacker_id, defender_id, selected_units):
    url = "http://127.0.0.1:8000"
    res = requests.get(url + f"/attack_opponent?attacker_id={attacker_id}&defender_id={defender_id}&selected_units={selected_units}")
    data = res.json()
    print(data["message"])

def turn_menu():
    print("\nWybierz akcję:")
    print("1. Wyświetl zasoby")
    print("2. Wyświetl budynki")
    print("3. Zbuduj budynek")
    print("4. Rekrutuj jednostki")
    print("5. Dodaj surowce")
    print("6. Wybierz jednostki do ataku")
    print("7. Zaatakuj przeciwnika")
    print("8. Zakończ turę")
    choice = int(input("Wybór: "))
    return choice

def play_turn(kraj_id):
    while True:
        choice = turn_menu()
        if choice == 1:
            print_resources(kraj_id)
        elif choice == 2:
            print_builds()
        elif choice == 3:
            print_builds()
            budynek_id = int(input("Wybierz co chcesz zbudować: "))
            build(kraj_id, budynek_id)
            print_resources(kraj_id)
        elif choice == 4:
            liczba = int(input("Ile chcesz jednostek: "))
            recruit(kraj_id, liczba)
            print_resources(kraj_id)
        elif choice == 5:
            print_dodane_surowce(kraj_id)
        elif choice == 6:
            selected_units = select_units(kraj_id)
            print(f"Wybrano {selected_units} jednostki do ataku.")
        elif choice == 7:
            defender_id = int(input("Wpisz ID kraju przeciwnika, który chcesz zaatakować: "))
            selected_units = select_units(kraj_id)
            attack_opponent(kraj_id, defender_id, selected_units)
        elif choice == 8:
            print("Tura zakończona.\n")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    id_wybrane = sprawdz_kraj()
    while True:
        play_turn(id_wybrane)
        next_turn = input("Czy chcesz rozpocząć następną turę? (tak/nie): ")
        if next_turn.lower() != 'tak':
            print("Gra zakończona.")
            break



