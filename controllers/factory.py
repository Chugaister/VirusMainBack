from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_session

from controllers.users import UsersController
from controllers.missings import MissingsController
from controllers.coincidences import CoincidencesController
from controllers.uploads import UploadsController


class ControllersFactory:

    @staticmethod
    def get_users_controller(session: AsyncSession = Depends(get_session)) -> UsersController:
        return UsersController(session)

    @staticmethod
    def get_missings_controller(session: AsyncSession = Depends(get_session)) -> MissingsController:
        return MissingsController(session)


    @staticmethod
    def get_concidences_controller(session: AsyncSession = Depends(get_session)) -> CoincidencesController:
        return CoincidencesController(session)

    @staticmethod
    def get_uploads_controller(session: AsyncSession = Depends(get_session)) -> UploadsController:
        return UploadsController(session)
