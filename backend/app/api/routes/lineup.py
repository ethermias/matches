from fastapi import APIRouter
from pydantic import BaseModel, conint
from typing import List

class Lineup(BaseModel):
    squad: List[conint(ge=0)]
    tag: str = None
    submission_time: str = None

router = APIRouter()

@router.post("/")
async def create_lineup(lineup: Lineup):
    current_time = datetime.now().isoformat()

    lineup.submission_time = current_time
    lineup_json = lineup.json()

    # Write JSON string to file
    with open("tags.json", "a") as f:
        f.write(lineup_json + "\n")

    return { "lineup": lineup }