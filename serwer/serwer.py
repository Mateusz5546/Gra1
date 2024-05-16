from fastapi import FastAPI
import main
import Function
import os
# try:
#     os.unlink("../gra.db")
# except:
#     pass




app = FastAPI()

main.zainicjuj()

@app.get("/countries")
def countries():
    return Function.name_country()
@app.get("/country/{kraj_id}")
def country(kraj_id):
    return Function.name_country_resorces(kraj_id)
@app.get("/structures")
def structure():
    return Function.name_build()
@app.get("/build_structure/{kraj_id}/{budynek_id}")
def build_structure(kraj_id:int,budynek_id:int):
    return Function.build_structure(budynek_id,kraj_id)
@app.get("/recruit_army")
def recruit_army(kraj_id:int,liczba_jednostek:int):
    return Function.recruit_army(kraj_id,liczba_jednostek)