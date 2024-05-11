from repositories.base import BaseRepository
from database.models.missing import Missing


class MissingsRepository(BaseRepository):

    def __init__(self):
        super().__init__(Missing)
