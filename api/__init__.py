from fastapi import APIRouter
from api.system.system import system_router
from api.users.users import users_router
from api.missings.missings import missings_router
from api.coincidences.coincidences import coincidences_router
from api.uploads.uploads import uploads_router

router = APIRouter(prefix="/v1")
router.include_router(system_router, prefix="/system")
router.include_router(users_router, prefix="/users")
router.include_router(missings_router, prefix="/missings")
router.include_router(coincidences_router, prefix="/coincidences")
router.include_router(uploads_router, prefix="/uploads")
