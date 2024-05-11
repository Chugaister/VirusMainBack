from pydantic import Field
from schemas.base.missings import MissingBase


class MissingResponse(MissingBase):
    missing_id: int = Field(example=12345)
