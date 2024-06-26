from fastapi.testclient import TestClient
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app, get_db
from database import Base



SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

""" 
poolclass=StaticPool : 
A connection pool is a standard technique used to maintain 
long running connections in memory for efficient re-use, 
as well as to provide management for the total number 
of connections an application might use simultaneously.

"""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_insert_new_element():
    response = client.post(
        "/insert_element/",
        json={"Element": "pommes", "Quantity": 5, "Unit": "unité"}
    )
    assert response.status_code == 422
