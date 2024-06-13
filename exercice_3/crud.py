from sqlalchemy.orm import Session
import models, schemas

def get_element(db: Session, element: str):
    return db.query(models.Courses).filter(models.Courses.Element == element).first()

def insert_element(db: Session, item: schemas.Item):
    new_element = models.Courses(
        Element = item.Element, 
        Quantity = item.Quantity, 
        Unit = item.Unit)
    db.add(new_element)
    db.commit()
    db.refresh(new_element)
    return new_element

def get_elements(db: Session, skip: int = 0,limit : int = 100):
    return db.query(models.Courses).offset(skip).limit(limit=limit).all()