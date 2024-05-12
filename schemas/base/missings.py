from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl
from datetime import date
from enum import Enum
from typing import Optional


class Gender(str, Enum):
    male = "male"
    female = "female"


class MissingBase(BaseModel):
    source_url: Optional[HttpUrl] = Field(example="https://wanted.mvs.gov.ua/searchbezvesti/")
    disappearance_date: Optional[date] = Field(example="2024-05-11")
    disappearance_place: Optional[str] = Field(example="Донецька обл, Покровський район, с. Хапотронівка")
    surname: str = Field(example="Парасюк")
    name: str = Field(example="Микола")
    father_name: str = Field(example="Іванович")
    surname_rus: Optional[str] = Field(example="Парасюк")
    name_rus: Optional[str] = Field(example="Николай")
    father_name_rus: Optional[str] = Field(example="Иванович")
    date_of_birth: date = Field(example="2024-05-11")
    gender: Optional[Gender] = Field(example="male")
    description: Optional[str] = Field(example="Опис зовнішності")
    special_data: Optional[str] = Field(example="Особливі прикмети")
    contact_data: Optional[str] = Field(example="+380000000000")
