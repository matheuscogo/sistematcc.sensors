from sqlalchemy import Column, DateTime, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ...db import db


class Confinamento(db):
    __tablename__ = "confinamento"
    id = Column("id", Integer, primary_key=True)
    planoId = Column(Integer, ForeignKey("planos.id"))
    matrizId = Column(Integer, ForeignKey("matrizes.id"))
    dataConfinamento = Column("dataConfinamento", DateTime)
    active = Column("active", Boolean, default=True)

    matrizes = relationship("Matriz", foreign_keys=matrizId)
    planos = relationship("Plano", foreign_keys=planoId)
