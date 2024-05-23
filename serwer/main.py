import Function
import os
import sqlite3




def tabela():
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='kraj' ''')
        tabela = cur.fetchone()
        if not tabela:
            cur.execute('''CREATE TABLE IF NOT EXISTS kraj
                     (id INTEGER PRIMARY KEY,
                      nazwa TEXT NOT NULL,
                      drewno INTEGER,
                      stal INTEGER,
                      jedzenie INTEGER,
                      liczba_jednostek INTEGER)''')
        else:
            print("Tabela 'kraj' już istnieje.")


def przpis_kraj():
    con = sqlite3.connect("../gra.db")
    cur = con.cursor()

    with open('podstawowy.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            cur.execute("INSERT INTO kraj (id, nazwa, drewno, stal,jedzenie,liczba_jednostek) VALUES (?, ?, ?, ?, ?,?)",
                        [v.strip() for v in values])

    con.commit()
    con.close()


def tabela_budynek():
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS typ_budynku
                     (id INTEGER PRIMARY KEY,
                      nazwa TEXT NOT NULL,
                      drewno INTEGER,
                      stal INTEGER,
                      jedzenie INTEGER)''')


def przpis_budynek():
    con = sqlite3.connect("../gra.db")
    cur = con.cursor()

    with open('budynki.txt', 'r', encoding="UTF-8") as file:
        for line in file:
            values = line.strip().split(',')
            cur.execute("INSERT INTO typ_budynku (id, nazwa, drewno, stal,jedzenie) VALUES (?, ?, ?, ?, ?)",
                        [v.strip() for v in values])

    con.commit()
    con.close()


def tabela_typ_jednostki():
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS typ_jednostki
                     (id INTEGER PRIMARY KEY,
                      nazwa TEXT NOT NULL,
                      drewno INTEGER,
                      stal INTEGER,
                      jedzenie INTEGER,
                      budynek_id INTEGER NOT NULL,
                      FOREIGN KEY(budynek_id) REFERENCES typ_budynku(id))''')


def przpis_jednostka():
    con = sqlite3.connect("../gra.db")
    cur = con.cursor()

    with open('jednostki.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            cur.execute(
                "INSERT INTO typ_jednostki (id, nazwa, drewno, stal,jedzenie,budynek_id) VALUES (?, ?, ?, ?, ?, ?)",
                [v.strip() for v in values])
    con.commit()
    con.close()


def tabela_kraj_budynku():
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS kraj_budynek
                      (liczba INTEGER,
                       budynek_id INTEGER NOT NULL,
                        kraj_id INTEGER NOT NULL,
                      FOREIGN KEY(budynek_id) REFERENCES typ_budynku(id),
                      FOREIGN KEY(kraj_id) REFERENCES kraj(id),
                      PRIMARY KEY(budynek_id,kraj_id))''')


def tabela_kraj_jednostka():
    with sqlite3.connect("../gra.db") as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS kraj_jednostka
                      (liczba INTEGER,
                       jednostka_id INTEGER NOT NULL,
                        kraj_id INTEGER NOT NULL,
                      FOREIGN KEY(jednostka_id) REFERENCES typ_jednostki(id),
                      FOREIGN KEY(kraj_id) REFERENCES kraj(id),
                      PRIMARY KEY(jednostka_id,kraj_id))''')

def czy_istnieje_baza():
    return os.path.isfile("../gra.db")
def zainicjuj():
    if not czy_istnieje_baza():
        tabela()
        przpis_kraj()
        tabela_budynek()
        przpis_budynek()
        tabela_typ_jednostki()
        przpis_jednostka()
        tabela_kraj_budynku()
        tabela_kraj_jednostka()
