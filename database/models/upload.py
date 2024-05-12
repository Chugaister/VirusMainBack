from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import FLOAT

from database.base import Base
from database.mixins.timestamp import TimestampMixin


class Upload(Base, TimestampMixin):
    __tablename__ = "photos"
    upload_id = Column(Integer, primary_key=True)
    missing_id = Column(Integer, ForeignKey("missings.missing_id"), unique=True)
    coincidence_id = Column(Integer, ForeignKey("coincidences.coincidence_id"), unique=True)
    media_type = Column(String, nullable=False)
    content = Column(BYTEA, nullable=False)
    embeddings = Column(ARRAY(FLOAT))
    missing = relationship("Missing", back_populates="uploads")
    coincidence = relationship("Coincidence", back_populates="uploads")
