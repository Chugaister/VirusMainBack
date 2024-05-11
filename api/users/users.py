from fastapi import APIRouter
from fastapi import Depends

from controllers.users import UsersController
from controllers.factory import ControllersFactory
from schemas.requests.users import RegisterUserTelegramRequest
from schemas.responses.users import UserResponse
from database.models.user import User
from utils.dependencies import get_current_user

users_router = APIRouter(tags=["Authentication"])


@users_router.post("/register")
async def register_user(
        register_user_request: RegisterUserTelegramRequest,
        users_controller: UsersController = Depends(ControllersFactory.get_users_controller)
) -> UserResponse:
    user = await users_controller.register_user(
        register_user_request.telegram_id,
        register_user_request.username,
        register_user_request.first_name,
        register_user_request.last_name,
        register_user_request.phone_number
    )
    return user


@users_router.post("/me")
async def get_me(
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    return current_user
