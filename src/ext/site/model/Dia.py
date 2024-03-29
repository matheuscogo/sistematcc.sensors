from sqlalchemy import Column, Integer, ForeignKey
from ext.db import db


class Dia(db):
    __tablename__ = "dias"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    planoId = Column("planos_id", Integer,  ForeignKey("planos.id"))
    dia = Column("dia", Integer)
    quantidade = Column("quantidade", Integer)
