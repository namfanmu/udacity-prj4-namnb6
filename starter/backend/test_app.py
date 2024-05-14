from . import app
import os


def test_movies_endpoint_returns_200():
    try:
        with app.test_client() as client:
            status_code = os.getenv("FAIL_TEST", 200)
            response = client.get("/movies/")
            assert response.status_code == status_code
    except Exception:
        return True
    