from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import Field
from datetime import date
from typing import Optional


class CoincidenceBase(BaseModel):
    source_url: Optional[HttpUrl] = Field(example="https://youtube.com")
    date_published: Optional[date] = Field(example="2024-05-11")

