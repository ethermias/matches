from fastapi import APIRouter
from pydantic import BaseModel, conint
from typing import List

class Lineup(BaseModel):
    squad: List[conint(ge=0)]
    tag: str = None

router = APIRouter()

@router.post("/")
async def create_lineup(lineup: Lineup):
    # Save to S3 or Database 
    return {"sr": lineup}
