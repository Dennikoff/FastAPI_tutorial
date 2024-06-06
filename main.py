from fastapi import FastAPI
from pydantic import BaseModel

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
def get_trades(limit: int = 10, offset: int = 0):
    return trades[offset:][:limit]

@app.patch("/users/{user_id}")
def change_user_name(user_id: int, name:str):
    for user in users:
        if user.get("id") == user_id:
            user["name"] = name
            return user
    print(users)
    return "404"

class Trade(BaseModel):
    id: int
    user_id: int
    amount: int

@app.post("/trade")
def add_trade(trade: Trade):
    trades.append(trade)
    return {"data": trades}