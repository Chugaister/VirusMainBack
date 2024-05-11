from fastapi import APIRouter
from fastapi import Query
from fastapi import Depends
from typing import List
from datetime import date

from schemas.requests.missings import CreateMissingRequest
from schemas.responses.missings import MissingResponse
from schemas.responses.coincidences import CoincidenceResponse

missings_router = APIRouter(tags=["Missing people adverts flow"])


@missings_router.post("/")
async def create_missing(
        create_missing_request: CreateMissingRequest,
        #missings_controller: MissingsController = Depends(ControllersFactory.get_missings_controller)
) -> MissingResponse:
    pass


@missings_router.get("/")
async def find_missing(
        surname: str = Query(example="Парасюк"),
        name: str = Query(example="Микола"),
        father_name: str = Query(example="Іванович"),
        date_of_birth: date = Query(example="2024-05-11")
) -> List[MissingResponse]:
    pass


@missings_router.get("/{missing_id}")
async def get_missing_by_id(
        missing_id: int,
        #missings_controller: MissingsController = Depends(ControllersFactory.get_missings_controller)
) -> MissingResponse:
    pass


@missings_router.get("/search/{missing_id}")
async def search(
        missing_id: int,
        #missings_controller: MissingsController = Depends(ControllersFactory.get_missings_controller)
) -> List[CoincidenceResponse]:
    pass
