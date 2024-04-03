from fastapi import APIRouter

router = APIRouter()
@router.get("/")
async def changelog():
  
    return {
        "v0.1.0": "init",
        "v0.1.1": "set up static site, adding dns ethermias.com, Mar 23, 2024",
        "v0.1.2": "set up dynamic site, setup kubernates claster, major upgrade UI, Mar 29, 2024",
        "v0.1.3": "Score update, Apr 05, 2024"
    }
    
