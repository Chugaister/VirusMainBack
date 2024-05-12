from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from typing import List

from controllers.base import BaseController
from repositories.coincidences import CoincidencesRepo
from repositories.missings import MissingsRepository
from database.models.coincidence import Coincidence
from database.models.missing import Missing
from exceptions.base import NotFoundException
from exceptions.base import BadRequestException


class CoincidencesController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.coincidences_repo = CoincidencesRepo()
        self.missing_repo = MissingsRepository()

    async def create(
            self,
            source_url: str,
            date_published: date
    ) -> Coincidence:
        coincidence = await self.coincidences_repo.create(
            self.session,
            attributes={
                "source_url": str(source_url),
                "date_published": date_published
            }
        )
        await self.session.commit()
        coincidence = await self.coincidences_repo.get_by(
            self.session,
            "coincidence_id",
            coincidence.coincidence_id,
            unique=True
        )
        return coincidence

    async def seek(
            self,
            missing_id: int
    ) -> List[Coincidence]:
        missing: Missing = await self.missing_repo.get_by(
            self.session,
            "missing_id",
            missing_id,
            unique=True
        )
        if not missing:
            raise NotFoundException("Missing not found")
        if not missing.uploads:
            raise BadRequestException("Missing's photo is not found")
        coincidences = await self.coincidences_repo.seek(
            self.session,
            missing.uploads[0].content
        )
        return coincidences


