from fastapi import APIRouter

router = APIRouter()
@router.get("/")
async def schedule():
    with open('/backend/data/teams/teams.json') as file:
        data = json.load(file)
    return [{ p["abbr"]: {"score": 0, "missPenality": 0, "red": 0, "yellow": 0} } for p in data ]
