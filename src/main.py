from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError

app = FastAPI(title="Trading App")

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )

users = [
    {"id": 1, "name": "Alex", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "junior"},
    ]},
    {"id": 2, "name": "Denis"},
    {"id": 3, "name": "Ilya"},
    {"id": 4, "name": "Andy"}
]

class DegreeType(Enum):
    juniour = "junior"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int
    name: str
    degree: Optional[List[Degree]] = []

@app.get("/users/")
def get_users():
    return {"users": users}

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user_id][0]


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
    amount: int = Field(ge=0)

@app.post("/trade")
def add_trade(trade: Trade):
    trades.append(trade)
    return {"data": trades}