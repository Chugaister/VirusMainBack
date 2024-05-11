from datetime import datetime, timedelta
from exceptions.base import UnauthorizedException
from utils.config import config
from jwt import decode, encode, ExpiredSignatureError, InvalidTokenError


class JWTHandler:
    secret_key = config.SECRET_KEY
    algorithm = "HS256"
    expire_time = timedelta(days=14)

    @staticmethod
    def encode(payload: dict, type_: str) -> str:
        expire = datetime.utcnow() + JWTHandler.expire_time
        payload.update({"exp": expire})
        return encode(
            payload, JWTHandler.secret_key, algorithm=JWTHandler.algorithm
        )

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return decode(
                token, JWTHandler.secret_key, algorithms=[JWTHandler.algorithm]
            )
        except ExpiredSignatureError as exception:
            raise UnauthorizedException("TokenExpired") from exception
        except InvalidTokenError as exception:
            raise UnauthorizedException("Invalid token") from exception

    @staticmethod
    def decode_expired(token: str) -> dict:
        try:
            return decode(
                token,
                JWTHandler.secret_key,
                algorithms=[JWTHandler.algorithm],
                options={"verify_exp": False},
            )
        except InvalidTokenError as exception:
            raise UnauthorizedException("Invalid token") from exception
