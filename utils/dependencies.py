from fastapi import Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.user import User
from database.session import get_session
from repositories.users import UsersRepository
from exceptions.base import UnauthorizedException


async def get_current_user(
        telegram_id: int = Query(example=123456789),
        session: AsyncSession = Depends(get_session)
) -> User:
    user_repo = UsersRepository()
    user: User = await user_repo.get_by(session, "telegram_id", telegram_id, unique=True)
    if not user:
        raise UnauthorizedException("User not found")
    return user
