from app.main import create_app

app = create_app()


def test_should_return_not_found_on_index():
    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 404


def test_fibonacci_should_return_no_content_when_query_string_is_absent():
    with app.test_client() as client:
        response = client.get("/fib")

        assert response.mimetype == "text/html"
        assert response.data == b""
        assert response.status_code == 204


def test_fibonacci_should_return_bad_request_on_non_number():
    with app.test_client() as client:
        response = client.get("/fib?n=a")

        assert response.status_code == 400


def test_fibonacci_should_return_bad_request_on_negative_number():
    with app.test_client() as client:
        response = client.get("/fib?n=-1")

        assert response.status_code == 400


def test_fibonacci_should_return_bad_request_on_high_number():
    with app.test_client() as client:
        response = client.get("/fib?n=101")

        assert response.status_code == 400


def test_fibonacci_should_return_correct_value_of_42():
    with app.test_client() as client:
        response = client.get("/fib?n=42")

        assert response.data == b"267914296"
        assert response.status_code == 200
