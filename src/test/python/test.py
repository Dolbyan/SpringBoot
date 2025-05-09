import requests
import time

def test_server():
    time.sleep(15)
    try:
        response = requests.get("http://localhost:8080")
        assert response.status_code == 404
    except requests.exceptions.ConnectionError:
        assert False, "Failed connection to server"

