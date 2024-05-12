from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy import Date
from sqlalchemy.orm import relationship
from typing import List

from database.base import Base
from database.mixins.timestamp import TimestampMixin


Gender = Enum(
    "male",
    "female",
    name="gender"
)


class Missing(Base, TimestampMixin):
    __tablename__ = "missings"
    missing_id = Column(Integer, primary_key=True)
    source_url = Column(String)
    disappearance_date = Column(Date)
    disappearance_place = Column(String)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    surname_rus = Column(String)
    name_rus = Column(String)
    father_name_rus = Column(String)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Gender)
    description = Column(String)
    special_data = Column(String)
    contact_data = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    uploads = relationship("Upload", back_populates="missing", lazy="selectin")

    @property
    def upload_ids(self) -> List[int]:
        return [upload.upload_id for upload in self.uploads]

