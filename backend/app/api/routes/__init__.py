from fastapi import APIRouter

from app.api.routes.teams import router as teams_router
from app.api.routes.lineup import router as lineup_router



router = APIRouter()


router.include_router(teams_router, prefix="/teams", tags=["teams"])
router.include_router(lineup_router, prefix="/lineup", tags=["lineup"])