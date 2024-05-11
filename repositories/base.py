from typing import Any, Generic, Type, TypeVar, Optional, Union
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select
from database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Base class for data repositories."""

    def __init__(self, model: Type[ModelType]):
        self.model_class: Type[ModelType] = model

    async def create(self, session: AsyncSession, attributes: dict[str, Any] = None) -> ModelType:
        if attributes is None:
            attributes = {}
        model = self.model_class(**attributes)
        session.add(model)
        return model

    async def get_all(
            self, session: AsyncSession, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        query = self.query()
        query = query.offset(skip).limit(limit)
        return await self.all(session, query)

    async def get_by(
            self,
            session: AsyncSession,
            field: str,
            value: Any,
            unique: bool = False,
    ) -> Union[ModelType, list[ModelType]]:
        query = self.query()
        query = await self._get_by(query, field, value)
        if unique:
            return await self.one(session, query)
        else:
            return await self.all(session, query)

    async def get_by_id(
            self,
            session: AsyncSession,
            value: Any,
    ) -> ModelType:
        query = self.query()
        query = await self._get_by(query, self.model_class.id_field_name, value)
        return await self.one(session, query)

    async def delete(self, session: AsyncSession, model: ModelType) -> None:
        await session.delete(model)

    def query(
            self,
            order_: Optional[dict] = None,
    ) -> Select:
        query = select(self.model_class)
        query = self._maybe_ordered(query, order_)
        return query

    async def all(self, session: AsyncSession, query: Select) -> list[ModelType]:
        result = await session.execute(query)
        return list(result.scalars().all())

    async def one(self, session: AsyncSession, query: Select) -> ModelType:
        result = await session.execute(query)
        return result.scalars().first()

    async def _get_by(self, query: Select, field: str, value: Any) -> Select:
        return query.where(getattr(self.model_class, field) == value)

    def _maybe_ordered(self, query: Select, order_: Optional[dict] = None) -> Select:
        if order_:
            if order_["asc"]:
                for order in order_["asc"]:
                    query = query.order_by(getattr(self.model_class, order).asc())
            else:
                for order in order_["desc"]:
                    query = query.order_by(getattr(self.model_class, order).desc())
        return query
