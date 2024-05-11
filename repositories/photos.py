from repositories.base import BaseRepository
from database.models.upload import Upload


class PhotosRepository(BaseRepository):

    def __init__(self):
        super().__init__(Upload)
