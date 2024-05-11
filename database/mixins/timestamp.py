from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:

    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime(timezone=True),
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
