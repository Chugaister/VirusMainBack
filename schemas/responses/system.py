from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class PongResponse(BaseModel):
    message: Optional[str] = Field(default="pong")
