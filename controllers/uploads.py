from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from database.models.upload import Upload
from controllers.base import BaseController
from repositories.uploads import UploadsRepo
from exceptions.base import NotFoundException
from exceptions.base import BadRequestException
from utils.facerecon import find_face_embeddings


class UploadsController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.uploads_repo = UploadsRepo()

    async def create(
            self,
            missing_id: int,
            coincidence_id: int,
            media_type: str,
            content: bytes
    ) -> None:
        embeddings = find_face_embeddings(content)
        print(embeddings)
        await self.uploads_repo.create(
            self.session,
            attributes={
                "missing_id": missing_id,
                "coincidence_id": coincidence_id,
                "media_type": media_type,
                "embeddings": embeddings,
                "content": content
            }
        )
        try:
            await self.session.commit()
        except IntegrityError:
            raise BadRequestException("Unable to post an upload")

    async def get_by_id(
            self,
            upload_id: int
    ) -> Upload:
        upload: Upload = await self.uploads_repo.get_by(self.session, "upload_id", upload_id, unique=True)
        if not upload:
            raise NotFoundException("Upload not found")
        return upload
