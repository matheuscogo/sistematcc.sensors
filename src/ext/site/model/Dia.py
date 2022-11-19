from sqlalchemy import Column, Integer, ForeignKey, DateTime
from ext.db import db

class Dia(db):
    __tablename__ = "dias"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    planoId = Column("plano_id", Integer,  ForeignKey("sistemaTCC.planos.id"))
    dia = Column("dia", Integer)
    quantidade = Column("quantidade", Integer)
