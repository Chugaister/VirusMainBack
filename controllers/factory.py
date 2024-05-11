from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_session

from controllers.users import UsersController


class ControllersFactory:

    @staticmethod
    def get_users_controller(session: AsyncSession = Depends(get_session)) -> UsersController:
        return UsersController(session)
