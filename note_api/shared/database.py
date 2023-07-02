from fastapi import Depends

from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy.inspection import inspect


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Self, List
    from sqlalchemy import Select, Insert, Update, Delete


from shared.settings import settings

engine = create_engine(settings.DB_URI, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class OrmBase(DeclarativeBase):
    """Extend the SQLAlchemy functionalities throught this class."""
