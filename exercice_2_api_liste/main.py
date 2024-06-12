from fastapi import FastAPI, HTTPException

app = FastAPI()

liste_courses = {}

"""
liste_courses = {
"pommes" : {"Q": 5, "U": "u"},
"Lait" : {"Q": 5, "U": "l"},
"bananes" : {"Q": 4, "U": "u"},
}
"""

@app.get("/")
def index():
    return {"message": "bonjour bienvenu sur l’API liste de course"}


@app.get('/get_list')
def get_list():
    if not liste_courses:
        return {"message": "La liste est vide"}
    else:
        return liste_courses
    

@app.post('/add_to_list')
def add_to_list(element:str, quantity:int, unit:str|None = ""):
    quantity_unit = {}
    if element in liste_courses:
        if unit == liste_courses[element]["U"]:
            liste_courses[element]["Q"] += quantity
            return {element : liste_courses[element]}
        else:
            raise HTTPException(status_code=400, 
                                detail=f"L'unité ne correspond pas {element} est en {liste_courses[element]['U']}"
                                )
    else:
        if unit:

            quantity_unit["Q"] = quantity
            quantity_unit["U"] = unit
            liste_courses[element] = quantity_unit
            return {element : liste_courses[element]}
        
        else:
            raise HTTPException(status_code=400, 
                                detail=f"Vous devez indiquer une unité pour {element} "
                                )

    
@app.delete('/remove_from_list')
def remove_from_liste(element:str):
    if element in liste_courses:
        del liste_courses[element]
        return liste_courses
    else:
        raise HTTPException(status_code=404, detail="Élément non trouvé dans la liste de courses")
    


@app.delete('/clean_list')
def clear_liste():
    liste_courses.clear()
    return liste_courses