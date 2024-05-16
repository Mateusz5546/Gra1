import sqlite3
def name_country():
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM kraj")
        return cur.fetchall()

def name_country_resorces(kraj_id):
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM kraj Where id=?", (kraj_id,))
        return cur.fetchone()

def choose_country(podstawowy, number):
    with open(podstawowy, 'r') as plik:
        first_line = plik.readline().strip()
        countries = first_line.split(',')
        for country_info in countries:
            if country_info.startswith(number):
                country = country_info[len(number):].strip()
                print("Wybrano kraj:", country)
                return country
    print("Kraj o podanym numerze nie istnieje.")
    return None

def recruit_army(kraj_id, liczba_jednostek):
    con = sqlite3.connect("../gra.db")
    cur = con.cursor()

    cur.execute("SELECT drewno, stal, jedzenie FROM kraj WHERE id = ?", (kraj_id,))
    resources = cur.fetchone()
    drewno, stal, jedzenie = resources
    con.commit()


    cur = con.cursor()
    cur.execute("SELECT drewno, stal, jedzenie FROM typ_jednostki")
    resources_jednostki =cur.fetchone()
    drewno_jednostki , stal_jednostki , jedzenie_jednostki  = resources_jednostki
    required_drewno = drewno_jednostki * liczba_jednostek
    required_stal = stal_jednostki * liczba_jednostek
    required_jedzenie = jedzenie_jednostki * liczba_jednostek

    # required_drewno -= int(required_drewno)
    # required_stal -= int(required_stal)
    # required_jedzenie -= int(required_jedzenie)

    if drewno >= required_drewno and stal >= required_stal and jedzenie >= required_jedzenie:
        new_drewno = drewno - required_drewno
        new_stal = stal - required_stal
        new_jedzenie = jedzenie - required_jedzenie

        cur.execute("UPDATE kraj SET drewno = ?, stal = ?, jedzenie = ? WHERE id = ?",
                    (new_drewno, new_stal, new_jedzenie, kraj_id))

        con.commit()
        cur = con.cursor()
        cur.execute("SELECT liczba FROM kraj_jednostka WHERE kraj_id = ?", (kraj_id,))
        tabela_liczba_jednostek = cur.fetchone()
        new_liczba_jednostek = tabela_liczba_jednostek + liczba_jednostek
        cur.execute("UPDATE kraj_jednostka SET liczba = ?, Where kraj_id = ?", (new_liczba_jednostek, kraj_id))
        con.commit()
        con.close()
        return {
            "message": "Successfully recruited {} armies.".format(liczba_jednostek),
            'resources': [required_drewno, required_stal, required_jedzenie]
        }
    else:
        return {
            "error": "Insufficient resources to recruit armies."
        }
def build_structure(budynek_id,kraj_id):

    con = sqlite3.connect("../gra.db")
    cur = con.cursor()
    cur.execute("SELECT drewno, stal, jedzenie FROM typ_budynku WHERE id = ?", (budynek_id,))
    required = cur.fetchone()
    required_drewno, required_stal, required_jedzenie =required
    con.commit()

    cur = con.cursor()
    cur.execute("SELECT drewno, stal, jedzenie FROM kraj WHERE id = ?", (kraj_id,))
    resources = cur.fetchone()
    drewno, stal, jedzenie = resources


    if drewno >= required_drewno and stal >= required_stal and jedzenie >= required_jedzenie:
        new_drewno = drewno - required_drewno
        new_stal = stal - required_stal
        new_jedzenie = jedzenie - required_jedzenie


        cur.execute("UPDATE kraj SET drewno = ?, stal = ?, jedzenie = ? WHERE id = ?",
                    (new_drewno, new_stal, new_jedzenie, budynek_id))

        # recruit_buff = 0.1
        # cur.execute("UPDATE kraj SET army_buff = ? WHERE id = ?", (recruit_buff, budynek_id))

        con.commit()
        con.close()
        return {
            "message": "Successfully built the structure and applied a recruitment buff."
        }
    else:
        return {
            "error": "Brak surowcow"
        }
def select_units(kraj_id):
    con = sqlite3.connect("../gra.db")
    cur = con.cursor()

    cur.execute("SELECT liczba FROM kraj_jednostka WHERE kraj_id = ?", (kraj_id,))
    num_units = cur.fetchone()[0]

    selected_units = int(input("Enter the number of units you want to use for the attack (max {}): ".format(num_units)))

    if selected_units <= num_units:
        return selected_units
    else:
        print("Invalid number of units selected.")
    return 0

def attack_opponent(attacker_id, defender_id, selected_units):
    con = sqlite3.connect("../gra.db")
    cur = con.cursor()

    cur.execute("SELECT liczba FROM kraj_jednostka WHERE kraj_id = ? AND jednostka_id = ?", (attacker_id, 1))
    attacker_units = cur.fetchone()[0]

    cur.execute("SELECT liczba FROM kraj_jednostka WHERE kraj_id = ? AND jednostka_id = ?", (defender_id, 1))
    defender_units = cur.fetchone()[0]

    if selected_units <= attacker_units:
        if selected_units >= defender_units:
            print("Congratulations! You have won the battle.")
            cur.execute("UPDATE kraj_jednostka SET liczba = ? WHERE kraj_id = ? AND jednostka_id = ?", (attacker_units - selected_units, attacker_id, 1))
            cur.execute("UPDATE kraj_jednostka SET liczba = ? WHERE kraj_id = ? AND jednostka_id = ?", (0, defender_id, 1))
        else:
            print("Unfortunately, you have lost the battle.")
            cur.execute("UPDATE kraj_jednostka SET liczba = ? WHERE kraj_id = ? AND jednostka_id = ?", (attacker_units - selected_units, attacker_id, 1))
    else:
        print("You don't have enough units to perform this attack.")
    con.commit()
    con.close()
    con.close()


# def game_turn(kraj_id):
#     turn_counter = 0
#
#     while True:
#         turn_counter += 1
#         print("\nTurn", turn_counter)
#         print("Turn Options:")
#         print("1. Recruit Army")
#         print("2. Build Structure")
#         print("3. Select Army")
#         print("4. Attack Opponent")
#         print("5. End Turn")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             liczba_jednostek = int(input("Enter the number of armies to recruit: "))
#             result = recruit_army(kraj_id, liczba_jednostek)
#             if "error" in result:
#                 print("Error:", result["error"])
#             else:
#                 print("Success:", result["message"])
#
#         elif choice == "2":
#             budynek_id = int(input("Enter the ID of the structure to build: "))
#             result = build_structure(budynek_id, kraj_id)
#             if "error" in result:
#                 print("Error:", result["error"])
#             else:
#                 print("Success:", result["message"])
#
#         elif choice == "3":
#             selected_units = select_units(kraj_id)
#             print("Selected {} units for attack.".format(selected_units))
#
#         elif choice == "4":
#             defender_id = int(input("Enter the ID of the opponent to attack: "))
#             selected_units = select_units(kraj_id)
#             attack_opponent(kraj_id, defender_id, selected_units)
#
#         elif choice == "5":
#             print("Ending turn", turn_counter)
#             print("Summary of actions:")
#             print("Resources remaining after turn:", name_country_resorces(kraj_id))
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
