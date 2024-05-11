from repositories.base import BaseRepository
from database.models.coincidence import Coincidence


class CoincidencesRepo(BaseRepository):

    def __init__(self):
        super().__init__(Coincidence)

