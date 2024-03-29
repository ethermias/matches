import json
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
async def get_all_teams() -> List[dict]:
    with open('/backend/data/teams/teams.json') as file:
        data = json.load(file)
    return data
   

@router.get("/{abbr}")
async def get_all_players(abbr: str) -> List[dict]:
    with open('/backend/data/roasters/' + abbr + '.json') as file:
        data = json.load(file)
    return data
