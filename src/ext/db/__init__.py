from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine

db = declarative_base()
engine = create_engine("sqlite:///src/sistemaTCC.db", echo=True, future=True)
session = Session(engine, future=True)


def init_app():
    db.metadata.create_all(engine)
