from fastapi import APIRouter

from schemas.responses.system import PongResponse

system_router = APIRouter(tags=["System endpoints"])


@system_router.get("/ping")
async def pong() -> PongResponse:
    return PongResponse()
