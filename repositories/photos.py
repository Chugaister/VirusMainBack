from repositories.base import BaseRepository
from database.models.photos import Photo


class PhotosRepository(BaseRepository):

    def __init__(self):
        super().__init__(Photo)
