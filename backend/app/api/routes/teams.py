from typing import List
import json
import os

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_teams() -> List[dict]:
    print('********************************************************')
    current_directory = os.getcwd()
    if os.path.exists('/backend/data/teams/teams.json'):
        print("File exists.")
    else:
        print("File does not exist.")

    print("Current directory:", current_directory)
    with open('/backend/data/teams/teams.json') as file:
        data = json.load(file)
    return data
   

@router.get("/{abbr}")
async def get_all_players(abbr: str) -> List[dict]:
    with open('/backend/data/roasters/' + abbr + '.json') as file:
        data = json.load(file)
    return data