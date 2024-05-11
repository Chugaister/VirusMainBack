from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy import Date

from database.base import Base
from database.mixins.timestamp import TimestampMixin


Gender = Enum(
    "male",
    "female",
    name="user_role"
)


class Missing(Base, TimestampMixin):
    __tablename_ = "missings"
    missing_id = Column(Integer, primary_key=True)
    disappearance_date = Column(Date, nullable=False)
    disappearance_place = Column(String)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    surname_rus = Column(String, nullable=False)
    name_rus = Column(String, nullable=False)
    father_name_rus = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Gender)
    description = Column(String, nullable=False)
    special_data = Column(String)
    contact_data = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)