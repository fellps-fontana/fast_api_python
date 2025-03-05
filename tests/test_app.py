from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo veio"}


def test_read_html_deve_retornar_ok_e_html(client):
    response = client.get("/EXE")
    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Exercicio Requisicao </title>
    </head>
    <body>
        <div class="container">
            <h1>Olá, Mundo Veio</h1>
            <a href="#" class="btn btn-custom">
                <i class="fas fa-play"></i> Explodir mundo
            </a>
        </div>
    </body>
    </html>
    """
    )


def test_cliente_user(client):
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


def test_read_user(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "felipe",
                "email": "felipe@gmail.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "teste",
            "password": "asda",
            "email": "teste@gmail.com",
            "id": 1,
        },
    )
    assert response.json() == {"username": "teste", "email": "teste@gmail.com", "id": 1}


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.json() == {"message": "user deleted"}


def test_delete_user_inexist(client):
    response = client.delete("/user/10")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
