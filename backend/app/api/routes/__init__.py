from fastapi import APIRouter

from app.api.routes.teams import router as teams_router
from app.api.routes.lineup import router as lineup_router
from app.api.routes.schedule import router as schedule_router
from app.api.routes.rules import router as rules_router
from app.api.routes.changelog import router as changelog_router


router = APIRouter()


router.include_router(teams_router, prefix="/teams", tags=["teams"])
router.include_router(lineup_router, prefix="/lineup", tags=["lineup"])
router.include_router(schedule_router, prefix="/schedule", tags=["schedule"])
router.include_router(rules_router, prefix="/rules", tags=["rules"])
router.include_router(changelog_router, prefix="/changelog", tags=["changelog"])