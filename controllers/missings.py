from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from typing import List

from controllers.base import BaseController
from repositories.missings import MissingsRepository
from repositories.photos import PhotosRepository
from database.models.missing import Missing
from database.models.upload import Upload
from exceptions.base import NotFoundException
from schemas.base.missings import Gender
from utils.geo import address_to_coordinates


class MissingsController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.missings_repo = MissingsRepository()

    async def create_missing(
            self,
            source_url: str,
            disappearance_date: date,
            disappearance_place: str,
            surname: str,
            name: str,
            father_name: str,
            surname_rus: str,
            name_rus: str,
            father_name_rus: str,
            date_of_birth: date,
            gender: Gender,
            description: str,
            special_data: str,
            contact_data: str
   ) -> Missing:
        latitude, longitude = address_to_coordinates(disappearance_place)
        missing = await self.missings_repo.create(
            self.session,
            attributes={
                "source_url": str(source_url),
                "disappearance_date": disappearance_date,
                "disappearance_place": disappearance_place,
                "latitude": latitude,
                "longitude": longitude,
                "surname": surname,
                "name": name,
                "father_name": father_name,
                "surname_rus": surname_rus,
                "name_rus": name_rus,
                "father_name_rus": father_name_rus,
                "date_of_birth": date_of_birth,
                "gender": gender,
                "description": description,
                "special_data": special_data,
                "contact_data": contact_data
            }
        )
        await self.session.commit()
        missing = await self.get_missing_by_id(missing.missing_id)
        return missing

    async def get_missing_by_id(
            self,
            missing_id: int
    ) -> Missing:
        missing: Missing = await self.missings_repo.get_by(
            self.session,
            "missing_id",
            missing_id,
            unique=True
        )
        if not missing:
            raise NotFoundException("Missing not found")
        return missing

    async def find_missing(self, surname: str, date_of_birth: date) -> List[Missing]:
        missings = await self.missings_repo.search(self.session, surname, date_of_birth)
        return missings

