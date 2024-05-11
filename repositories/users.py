from repositories.base import BaseRepository
from database.models.user import User


class UsersRepository(BaseRepository):

    def __init__(self):
        super().__init__(User)


