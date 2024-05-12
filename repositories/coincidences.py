from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from repositories.base import BaseRepository
from database.models.coincidence import Coincidence
from utils.facerecon import find_face_embeddings
from utils.facerecon import compare_faces


class CoincidencesRepo(BaseRepository):

    def __init__(self):
        super().__init__(Coincidence)

    async def seek(self, session: AsyncSession, content: bytes) -> List[Coincidence]:
        emb = find_face_embeddings(content)
        query = self.query()
        coincidences = await self.all(session, query)
        result = []
        for coincidence in coincidences:
            if coincidence.uploads and compare_faces(emb, coincidence.uploads[0].embeddings):
                result.append(coincidence)
        return result


