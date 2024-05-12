from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from typing import List

from controllers.missings import MissingsController
from controllers.factory import ControllersFactory
from controllers.coincidences import CoincidencesController
from database.models.coincidence import Coincidence
from schemas.requests.coincidences import CreateCoincidenceRequest
from schemas.responses.coincidences import CoincidenceResponse

coincidences_router = APIRouter(tags=["Coincidences related endpoints"])


@coincidences_router.post("/")
async def create_coincidence(
        create_coincidence_request: CreateCoincidenceRequest,
        coincidence_controller: CoincidencesController = Depends(ControllersFactory.get_concidences_controller)
) -> CoincidenceResponse:
    coincidence = await coincidence_controller.create(
        create_coincidence_request.source_url,
        create_coincidence_request.date_published
    )
    return coincidence


@coincidences_router.get("/search")
async def seek_coincidences(
        missing_id: int = Query(example=123),
        coincidence_controller: CoincidencesController = Depends(ControllersFactory.get_concidences_controller)
) -> List[CoincidenceResponse]:
    coincidences = await coincidence_controller.seek(missing_id)
    return coincidences
