from fastapi import APIRouter
from fastapi import Query
from fastapi import Depends
from typing import List
from datetime import date

from controllers.missings import MissingsController
from controllers.factory import ControllersFactory
from schemas.requests.missings import CreateMissingRequest
from schemas.responses.missings import MissingResponse
from schemas.responses.coincidences import CoincidenceResponse

missings_router = APIRouter(tags=["Missing people adverts flow"])


@missings_router.post("/")
async def create_missing(
        create_missing_request: CreateMissingRequest,
        missings_controller: MissingsController = Depends(ControllersFactory.get_missings_controller)
) -> MissingResponse:
    missing = await missings_controller.create_missing(
        create_missing_request.source_url,
        create_missing_request.disappearance_date,
        create_missing_request.disappearance_place,
        create_missing_request.surname,
        create_missing_request.name,
        create_missing_request.father_name,
        create_missing_request.surname_rus,
        create_missing_request.name_rus,
        create_missing_request.father_name_rus,
        create_missing_request.date_of_birth,
        create_missing_request.gender,
        create_missing_request.description,
        create_missing_request.special_data,
        create_missing_request.contact_data
    )
    return missing


@missings_router.get("/{missing_id}")
async def get_missing_by_id(
        missing_id: int,
        missings_controller: MissingsController = Depends(ControllersFactory.get_missings_controller)
) -> MissingResponse:
    missing = await missings_controller.get_missing_by_id(missing_id)
    return missing


@missings_router.get("/")
async def find_missing(
        surname: str = Query(example="Парасюк"),
        name: str = Query(example="Микола"),
        father_name: str = Query(example="Іванович"),
        date_of_birth: date = Query(example="2024-05-11"),
        missings_controller: MissingsController = Depends(ControllersFactory.get_missings_controller)
) -> List[MissingResponse]:
    missings = await missings_controller.find_missing(
        surname,
        date_of_birth
    )
    return missings
