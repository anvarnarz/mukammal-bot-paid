from sqlalchemy import insert, select, update

from Repos import BaseSQLAlchemyRepo

class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(self, user_id: int, name: str, language: str, is_subscribed: bool, phone: str) -> None:
        sql = insert(self.model).values(
            user_id=user_id,
            name=name,
            language=language,
            is_subscribed=is_subscribed,
            phone=phone
        )
        await self._session.execute(sql)
        await self._session.commit()
