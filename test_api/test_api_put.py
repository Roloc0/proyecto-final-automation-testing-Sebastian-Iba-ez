import requests
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api_put_post():
    logging.info ("Iniciado el test_api_put_post")
    payload = {
        "id": 1,
        "title": "Titulo actualizado",
        "body": "Contenido actualizado",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=payload)

    # Validar código
    assert response.status_code == 200
    logging.info ("Codigo validado")

    # Validar que el JSON refleja el contenido enviado
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["id"] == 1
    logging.info ("Concluido el test_api_put_post")