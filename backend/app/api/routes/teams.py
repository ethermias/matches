import json
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from app.util.salaryMetrix import salaryMetrix as salaryMetrix

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
        data_with_stats = [d for d in data if 'stats' in d]
        for player in data_with_stats:
            player['salary'] = salaryMetrix(abbr, player)

    sorted_data = sorted(data_with_stats, key=lambda x: x['stats']['general']['appearances'], reverse=True)
    return sorted_data
