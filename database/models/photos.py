from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BYTEA

from database.base import Base
from database.mixins.timestamp import TimestampMixin


class Photo(Base, TimestampMixin):
    __tablename__ = "photos"
    photo_id = Column(Integer, primary_key=True)
    missing_id = Column(Integer, ForeignKey("missings.missing_id"))
    media_type = Column(String, nullable=False)
    content = Column(BYTEA, nullable=False)
    missing = relationship("Missing", back_populates="photos")
