from pydantic import Field
from schemas.base.missings import MissingBase
from typing import Optional
from typing import List


class MissingResponse(MissingBase):
    latitude: Optional[float] = Field(example=49.829069)
    longitude: Optional[float] = Field(example=24.013829)
    missing_id: int = Field(example=12345)
    
    upload_ids: List[int]
