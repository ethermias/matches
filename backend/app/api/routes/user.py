from fastapi import APIRouter
from pydantic import BaseModel
import json

class User(BaseModel):
    email: str = None
    userName: str = None
    submittedAt: str = None

class LogUser(BaseModel):
    user: User
    exists: bool

router = APIRouter()

def log_user(logUser: LogUser):
    with open("user_tags_log.json", "a") as f:
        f.write(logUser.json() + "\n")

@router.post("/signin")
async def sign_in_user(user: User):
    filename = "user_tags.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    exists = any((d['email'] == user.email or d['userName'] == user.userName) for d in data)
    log_user(LogUser(user=user, exists=exists))
    return { "user": user, "user_valid": exists }

@router.post("/signup")
async def sign_up_user(user: User):
    filename = "user_tags.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    exists = any((d['email'] == user.email or d['userName'] == user.userName) for d in data)
    log_user(LogUser(user=user, exists=exists))
    if not exists:
        data.append(user.dict())
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    return { "user": user, "user_created": not exists }
