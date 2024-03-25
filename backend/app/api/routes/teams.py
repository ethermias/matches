from typing import List
import csv

from fastapi import APIRouter

router = APIRouter()
teams = [
        "Arsenal",
        "Aston Villa",
        "Brentford",
        "Brighton & Hove Albion",
        "Burnley",
        "Chelsea",
        "Crystal Palace",
        "Everton",
        "Leeds United",
        "Leicester City",
        "Liverpool",
        "Manchester City",
        "Manchester United",
        "Newcastle United",
        "Norwich City",
        "Southampton",
        "Tottenham Hotspur",
        "Watford",
        "West Ham United",
        "Wolverhampton Wanderers"
    ]



@router.get("/")
async def get_all_teams() -> List[dict]:
 
    return [ { key: teams[key-1]} for key in range(1, 21) ]

@router.get("/{id}")
async def get_all_players(id: int) -> List[dict]:
    return [ { k: teams[id] + "-" + str(k)} for k in range(1, 26) ]