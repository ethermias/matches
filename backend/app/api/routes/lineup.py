from fastapi import APIRouter
from pydantic import BaseModel, conint
from typing import List

class Lineup(BaseModel):
    squad: List[conint(ge=0)]
    tag: str = None
    submittedAt: str = None

router = APIRouter()

@router.post("/")
async def create_lineup(lineup: Lineup):

    lineup_json = lineup.json()

    # Write JSON string to file
    with open("tags.json", "a") as f:
        f.write(lineup_json + "\n")

    return { "lineup": lineup }