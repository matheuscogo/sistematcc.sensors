from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ext.db import db


class Dia(db):
    __tablename__ = "dias"
    id = Column("id", Integer, primary_key=True)
    planoId = Column("planoId", Integer,  ForeignKey("planos.id"))
    dia = Column("dia", Integer)
    quantidade = Column("quantidade", Integer)

    plano = relationship("Plano", foreign_keys=planoId)
