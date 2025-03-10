from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse

from fest_api_zero.schemas import Message, UserDb, UserLIst, UserPublic, UserSchema

app = FastAPI()
database = []


@app.get("/", response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {"message": "Olá mundo veio"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create(user: UserSchema):
    user_with_id = UserDb(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get("/EXE", response_class=HTMLResponse, status_code=HTTPStatus.OK)
def read_html():
    return """
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


@app.get("/users/", response_model=UserLIst)
def read_users():
    return {"users": database}


@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    user_with_id = UserDb(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    del database[user_id - 1]
    return {"message": "user deleted"}
