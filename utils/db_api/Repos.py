from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession


class BaseSQLAlchemyRepo(ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
