from http import HTTPStatus
from fastapi import FastAPI
from starlette.responses import HTMLResponse
from fest_api_zero.schemas import Message


app = FastAPI()

@app.get("/", response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {"message": "Olá mundo veio"}


@app.get("/EXE", response_class=HTMLResponse, status_code=HTTPStatus.OK)
def read_html():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content7u88888888888888888="width=device-width, initial-scale=1.0">
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
