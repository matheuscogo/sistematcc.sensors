from sqlalchemy import Column, DateTime, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ext.db import db


class Inseminacao(db):
    __tablename__ = "inseminacao"
    id = Column("id", Integer, primary_key=True)
    planoId = Column(Integer, ForeignKey("planos.id"))
    matrizId = Column(Integer, ForeignKey("matrizes.id"))
    confinamentoId = Column(Integer, ForeignKey("confinamento.id"))
    dataInseminacao = Column("dataInseminacao", DateTime)
    active = Column("active", Boolean, default=True)

    matrizes = relationship("Matriz", foreign_keys=[matrizId])
    planos = relationship("Plano", foreign_keys=[planoId])
