from fastapi import FastAPI

app = FastAPI(title="Trading App")

users = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Denis"},
    {"id": 3, "name": "Ilya"},
    {"id": 4, "name": "Andy"}
]

@app.get("/users/")
def get_users():
    return {"users": users}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user": [user for user in users if user.get("id") == user_id][0]} 


trades = [
    {"id": 1, "user_id": 1, "amount": 133},
    {"id": 2, "user_id": 4, "amount": 412},
    {"id": 3, "user_id": 3, "amount": 5123},
    {"id": 4, "user_id": 2, "amount": 12},
]

@app.get("/trades")
def get_trades(limit: int, offset: int):
    return trades[offset:][:limit]