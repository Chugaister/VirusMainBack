from typing import List

from schemas.base.coincidences import CoincidenceBase


class CoincidenceResponse(CoincidenceBase):
    upload_ids: List[int]

