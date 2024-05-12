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
            if coincidence.uploads:
                is_same, accuracy = compare_faces(emb, coincidence.uploads[0].embeddings)
                if is_same:
                    result.append((coincidence, accuracy))
        result.sort(key=lambda x: x[1], reverse=True)
        return [r[0] for r in result]


