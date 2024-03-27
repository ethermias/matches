from fastapi import APIRouter

router = APIRouter()
@router.get("/")
async def changelog():
  
    return {
        "v0.1.0": "set up static site, adding dns ethermias.com",
        "v0.1.1": "set up dynamic site, setup kubernates claster, major upgrade UI"
    }
    
