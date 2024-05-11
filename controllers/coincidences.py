from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from controllers.base import BaseController
from repositories.coincidences import CoincidencesRepo
from database.models.coincidence import Coincidence


class CoincidencesController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.coincidences_repo = CoincidencesRepo()

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
