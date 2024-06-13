from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import schemas, models, crud
from database import Base, engine, SessionLocal

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

app = FastAPI()

liste_courses = {}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        # utiliser yield pour exécuter des étapes en plus
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"message": "bonjour bienvenue sur l’API liste de course change"}

@app.get("/home")
def home():
    return {"message": "Bonjour, bienvenue à la maison changement sur le local"}


@app.post("/insert_element", response_model= schemas.Item)
def insert_new_element(item:schemas.Item, db:Session = Depends(get_db)):

    new_element = crud.get_element(db, element= item.Element)
    if new_element:
        raise HTTPException(status_code=400, detail=f"{item.Element} disponible sur la lite")
    else:
        return crud.insert_element(db= db, item= item)
    
@app.get("/display_database")
def get_elements(skip: int=0, limit:int = 100, db:Session = Depends(get_db)):
    elements = crud.get_elements(db=db, skip=skip, limit=limit)
    return elements
