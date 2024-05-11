from fastapi import APIRouter
from fastapi import Query
from fastapi import UploadFile
from fastapi import File
from fastapi.responses import StreamingResponse
from fastapi import Depends
from io import BytesIO
from typing import Optional

from controllers.uploads import UploadsController
from controllers.factory import ControllersFactory
from schemas.responses.system import EntityCreated


uploads_router = APIRouter(tags=["Uploads related endpoints"])


@uploads_router.post("/")
async def upload_photo(
        missing_id: Optional[int] = Query(example=123, default=None),
        coincidence_id: Optional[int] = Query(example=123, default=None),
        media_type: Optional[str] = Query(example="image/jpeg"),
        file: UploadFile = File(),
        uploads_controller: UploadsController = Depends(ControllersFactory.get_uploads_controller)
) -> EntityCreated:
    await uploads_controller.create(
        missing_id,
        coincidence_id,
        media_type,
        await file.read()
    )
    return EntityCreated(message="Photo uploaded successfully")


@uploads_router.get("/{upload_id}")
async def upload_photo(
        upload_id: int,
        uploads_controller: UploadsController = Depends(ControllersFactory.get_uploads_controller)
) -> StreamingResponse:
    photo = await uploads_controller.get_by_id(upload_id)
    return StreamingResponse(content=BytesIO(photo.content), media_type=photo.media_type)
