from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import BYTEA

from database.base import Base
from database.mixins.timestamp import TimestampMixin


class Photo(Base, TimestampMixin):
    __tablename__ = "photos"
    photo_id = Column(Integer, primary_key=True)
    file_type = Column(String, nullable=False)
    content = Column(BYTEA, nullable=False)

