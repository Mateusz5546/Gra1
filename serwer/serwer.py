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
@app.get("/build_structure")
def build_structure(budynek_id:int, structure_id:int):
    return Function.build_structure(budynek_id, structure_id)
@app.get("/recruit_army")
def recruit_army(kraj_id:int,liczba_jednostek:int):
    return Function.recruit_army(kraj_id,liczba_jednostek)