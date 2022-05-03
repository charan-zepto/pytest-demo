from fastapi import Body, Depends, FastAPI
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import declarative_base

_engine = create_engine("sqlite:///test.db")
_session = sessionmaker(bind=_engine)


def SessionLocal():
    txn = _session()
    try:
        yield txn
        txn.commit()
    except Exception as exc:
        txn.rollback()


Base = declarative_base()


class KVPair(Base):
    __tablename__ = "pair"
    key = Column(String, primary_key=True)
    value = Column(String)


def on_start():
    Base.metadata.create_all(bind=_engine)
