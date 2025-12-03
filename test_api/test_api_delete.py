import requests
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api_delete_post():
    logging.info("Iniciando test_api_delete_post")
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code in (200, 204)
    logging.info("Concluido el test_api_delete_post")