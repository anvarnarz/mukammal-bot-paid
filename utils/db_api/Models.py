from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, func

from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=func.now())
    updated_at = Column(DateTime(True), default=func.now(), onupdate=func.now(), server_default=func.now())


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    chat_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)

    def __repr__(self):
        return f'{self.id} | {self.chat_id}'
