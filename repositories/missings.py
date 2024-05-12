from sqlalchemy.ext.asyncio import AsyncSession
from repositories.base import BaseRepository
from database.models.missing import Missing
from typing import List
from datetime import date


class MissingsRepository(BaseRepository):

    def __init__(self):
        super().__init__(Missing)

    async def search(
            self,
            session: AsyncSession,
            surname: str,
            date_of_birth: date
    ) -> List[Missing]:
        query = self.query().where(Missing.surname == surname).where(Missing.date_of_birth == date_of_birth)
        return await self.all(session, query)

    async def seek_coincidences(self, missing_id):
        pass
