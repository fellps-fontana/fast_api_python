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
    assert response.text.strip() == (
        '\n    <!DOCTYPE html>\n    <html lang="pt-br">\n    <head>\n'
        '        <meta charset="UTF-8">\n'
        '        <meta name="viewport" ' +
        'content="width=device-width, initial-scale=1.0">' +
        '\n'
        '        <title>Exercicio Requisicao </title>\n'
        '    </head>\n    <body>\n'
        '        <div class="container">\n'
        '            <h1>Olá, Mundo Veio</h1>\n'
        '            <a href="#" class="btn btn-custom">\n'
        '                <i class="fas fa-play"></i> Explodir mundo\n'
        '            </a>\n'
        '        </div>\n    </body>\n    </html>\n    '
    ).strip()
