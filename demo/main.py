from fastapi import Body, Depends, FastAPI
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import declarative_base
from demo import db


def create_app():
    app = FastAPI()

    app.add_event_handler("startup", db.on_start)

    app.post("/storage")(store)
    app.get("/storage")(fetch)

    return app


def store(
    key: str = Body(...),
    value: str = Body(...),
    session: Session = Depends(db.SessionLocal),
):
    session.add(db.KVPair(key=key, value=value))
    return "success"


def fetch(key: str, session: Session = Depends(db.SessionLocal)):
    pair = session.get(db.KVPair, key)
    return dict(key=pair.key, value=pair.value)
