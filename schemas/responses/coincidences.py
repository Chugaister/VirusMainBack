from typing import List

from schemas.base.coincidences import CoincidenceBase


class CoincidenceResponse(CoincidenceBase):
    coincidence_id: int
    upload_ids: List[int]

