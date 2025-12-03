import requests
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api_get_post():
    logging.info("Iniciando test_api_get_post")
    response = requests.get(f"{BASE_URL}/posts/1")


    # Validar código de estado
    assert response.status_code == 200
    logging.info ("codigo validado")

    # Validar estructura del JSON
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    assert "title" in data
    assert isinstance(data["title"], str)
    logging.info ("Concluido el test_api_get_post")