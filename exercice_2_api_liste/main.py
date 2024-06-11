from fastapi import FastAPI, HTTPException

app = FastAPI()

liste_courses = {}

@app.get("/")
def index():
    return {"message": "bonjour bienvenu sur l’API liste de course"}


@app.get('/liste')
def get_list():
    if not liste_courses:
        return {"message": "La liste est vide"}
    else:
        return liste_courses
    

@app.post('/liste')
def add_to_list(element:str, quantity:int, unit:str = ""):
    quantity_unit = {}
    if element in liste_courses:
        liste_courses[element]["Q"] += quantity
    else:
        quantity_unit["Q"] = quantity
        quantity_unit["U"] = unit
        liste_courses[element] = quantity_unit
    return liste_courses


@app.delete('/liste')
def remove_from_liste(element:str):
    if element in liste_courses:
        del liste_courses[element]
        return liste_courses
    else:
        raise HTTPException(status_code=404, detail="Élément non trouvé dans la liste de courses")
    


@app.delete('/liste/clear')
def clear_liste():
    liste_courses.clear()
    return liste_courses