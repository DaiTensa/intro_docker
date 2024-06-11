from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_get_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Salut tout le monde"}


def test_get_list():
    response = client.get("/liste")
    assert response.status_code == 200
    assert response.json() == {"content": []}

def test_add_to_list():
    response = client.post('/liste', params= {"element" : 1})
    assert response.status_code == 200
    assert response.json() == {"content": [1]}
    response = client.post('/liste', params= {"element" : "hello"})
    assert response.status_code == 422

def test_delete_element():
        client.post('/liste', json= {"element" : 1})
        response = client.delete('/liste', params= {"element" : 1})
        assert response.json() == {"content": []}
        response = client.delete('/liste', params= {"element" : "hello"})
        assert response.status_code == 422
        response = client.delete('/liste', params=  {"element" : 8})
        assert response.status_code == 404
        assert response.json() == {"detail": "Element not found in the list"}










