from pydantic import BaseModel
from pydantic import Field
from datetime import date
from enum import Enum
from typing import Optional


class Gender(str, Enum):
    male = "male"
    female = "female"


class MissingBase(BaseModel):
    disappearance_date: date = Field(example="2024-05-11")
    disappearance_place: Optional[str] = Field(example="Донецька обл, Покровський район, с. Хапотронівка")
    latitude: Optional[float] = Field(example=49.829069)
    longitude: Optional[float] = Field(example=24.013829)
    surname: str = Field(example="Парасюк")
    name: str = Field(example="Микола")
    father_name: str = Field(example="Іванович")
    surname_rus: str = Field(example="Парасюк")
    name_rus: str = Field(example="Николай")
    father_name_rus: str = Field(example="Иванович")
    date_of_birth: date = Field(example="2024-05-11")
    gender: Gender = Field(example="male")
    description: Optional[str] = Field(example="Опис зовнішності")
    special_data: Optional[str] = Field(example="Особливі прикмети")
    contact_data: str = Field(example="+380000000000")
