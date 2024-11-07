from fastapi import FastAPI, Path
from routers import user
from routers import task

app= FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)


# python -m uvicorn main:app