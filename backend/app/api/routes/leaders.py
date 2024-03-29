from fastapi import APIRouter

router = APIRouter()
@router.get("/")
async def leaders():
    return {
        "matchday": 30, 
        "total": 123,
        "leaders": [{
            "username": "tags",
            "tags": "tags",
            "formation": "4-4-2",
            "submited": "2024-02-21",
            "score": 17
        }]
    }
    
