from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.orm import relationship
from typing import List

from database.base import Base
from database.mixins.timestamp import TimestampMixin


class Coincidence(Base, TimestampMixin):
    __tablename__ = "coincidences"
    coincidence_id = Column(Integer, primary_key=True)
    source_url = Column(String)
    date_published = Column(Date)

    uploads = relationship("Upload", back_populates="coincidence", lazy="selectin")

    @property
    def upload_ids(self) -> List[int]:
        return [upload.upload_id for upload in self.uploads]


