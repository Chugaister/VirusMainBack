from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BIGINT
from sqlalchemy import String

from database.base import Base
from database.mixins.timestamp import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"
    telegram_id = Column(BIGINT, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)


