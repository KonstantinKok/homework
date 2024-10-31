from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome():
    return "Главная страница"

@app.get("/admin")   # сделал без user так как считаю это более правильным адресом для админ панели
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def id_paginator(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="75")) -> dict:
    return {"message": f"Hello {user_id}"}

@app.get("/user/{username}/{age}")
async def news(username: Annotated[ str, Path(min_length=5, max_length=20, description="Enter you username", example="montes")]
                                   , age: int, ge=18, le=120) -> dict:
    return {"message": f"Hello {username} {age}"}


# python -m uvicorn module_16_2:app