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

def get_matching_value(user, data):
    for d in data:
        if d['email'] == user.email or d['userName'] == user.userName:
            return d
    return None

@router.post("/signin")
async def sign_in_user(user: User):
    filename = "user_tags.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    exists = get_matching_value(user, data)
    log_user(LogUser(user=user, exists=exists != None))
    return {"user": exists if exists is not None else user, "isValid": exists != None}

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
    return { "user": user, "isValid": not exists }
