from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class UserBase(BaseModel):
    telegram_id: int = Field(example=123456789)
    username: Optional[str] = Field(example="johndoe")
    first_name: Optional[str] = Field(example="John")
    last_name: Optional[str] = Field(example="Doe")
    phone_number: Optional[str] = Field(example="+380000000000")



