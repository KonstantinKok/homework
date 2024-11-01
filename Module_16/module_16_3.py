from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/users/{username}/{age}")
async def post_users(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = username
    return f"User {users} is registered"

@app.put("/users/{user_id}/{username}/{age}'")
async def update_user(user_id: int, username: str, age: int) -> str:
    return f"The user {user_id} is registered"

@app.delete("/users/{user_id}")
async def delete_user(user_id:int) -> str:
    users.clear()
    return f"User {user_id} has been deleted"

# python -m uvicorn module_16_3:app