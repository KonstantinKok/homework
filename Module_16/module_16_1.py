from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return "Главная страница"

@app.get("/admin")   # сделал без user так как считаю это более правильным адресом для админ панели
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{id_name}")
async def news(id_name: str):
    return f"Вы вошли как пользователь №{id_name}"

@app.get("/id")
async def id_paginator(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


# python -m uvicorn module_16_1:app