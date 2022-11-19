from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine, func

db = declarative_base()
engine = create_engine(
    "sqlite:///../../projects/sistematcc.flask/srcsistemaTCC-old.db", echo=True, future=True)
session = Session(engine, future=True)
func = func


def init_app():
    db.metadata.create_all(engine)
