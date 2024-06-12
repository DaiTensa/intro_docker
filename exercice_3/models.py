from sqlalchemy import Column, Integer, String
from database import Base


class Courses(Base):
    __tablename__ = "courses"
    Element = Column(String, unique=True, primary_key=True, nullable=False, index=True)
    Quantity = Column(Integer, index=True)
    Unit = Column(String, index=True)
