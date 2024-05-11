from sqlalchemy.ext.asyncio import AsyncSession
from controllers.base import BaseController
from repositories.users import UsersRepository
from database.models.user import User
from exceptions.base import UnauthorizedException


class UsersController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repo = UsersRepository()
