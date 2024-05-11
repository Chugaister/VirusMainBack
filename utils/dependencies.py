from fastapi import Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.user import User
from database.session import get_session
from utils.security import JWTHandler
from repositories.users import UsersRepository
from exceptions.base import UnauthorizedException


async def get_current_user(access_token: str = Header(), session: AsyncSession = Depends(get_session)) -> User:
    access_token = JWTHandler.decode(access_token)
    user_repo = UsersRepository()
    user = await user_repo.get_by_id(session, access_token.get("user_id"))
    if not user:
        raise UnauthorizedException("User not found")
    return user
