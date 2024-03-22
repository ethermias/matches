from typing import List

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_all_teams() -> List[dict]:
    teams = [
        {"id": 1, "name": "Arasneal"},
        {"id": 2, "name": "Liverpool"},
        {"id": 3, "name": "City"}
    ]

    return teams