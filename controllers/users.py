from sqlalchemy.ext.asyncio import AsyncSession
from controllers.base import BaseController
from repositories.users import UsersRepository
from database.models.user import User
from exceptions.base import UnauthorizedException
from exceptions.base import BadRequestException


class UsersController(BaseController):

    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repo = UsersRepository()

    async def register_user(
            self,
            telegram_id: int,
            username: str,
            first_name: str,
            last_name: str,
            phone_number: str
    ) -> User:
        user = await self.user_repo.get_by(self.session, "telegram_id", telegram_id)
        if user:
            raise BadRequestException("User already registered")
        user = await self.user_repo.create(
            self.session,
            attributes={
                "telegram_id": telegram_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number
            }
        )
        await self.session.commit()
        return user
