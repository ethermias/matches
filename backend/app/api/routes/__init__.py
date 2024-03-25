from fastapi import APIRouter

from app.api.routes.teams import router as teams_router


router = APIRouter()


router.include_router(teams_router, prefix="/teams", tags=["teams"])