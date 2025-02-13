from http import HTTPStatus

from fastapi.testclient import TestClient

from fest_api_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo veio"}


def test_read_html_deve_retornar_ok_e_html():
    client = TestClient(app)
    response = client.get("/EXE")
    assert response.status_code == HTTPStatus.OK
    html_esperado = """<!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Exercicio Requisicao</title>
    </head>
    <body>
        <div class="container">
            <h1>Olá, Mundo Veio</h1>
            <a href="#" class="btn btn-custom">
                <i class="fas fa-play"></i> Explodir mundo
            </a>
        </div>
    </body>
    </html>"""

    assert normalize_html(response.text) == normalize_html(html_esperado)


def test_cliente_user():
    client = TestClient(app)
    response = client.post(
        "/users/",
        json={"username": "felipe", "password": "545", "email": "felipe@gmail.com"},
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "felipe",
        "email": "felipe@gmail.com",
        "id": 1,
    }
