from pydantic import BaseModel


class Item(BaseModel):
    Element : str
    Quantity : int
    Unit : str

    class Config:
        orm_mode = True