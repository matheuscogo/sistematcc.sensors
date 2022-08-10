from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ext.db import db


class Alimentador(db):
    __tablename__ = "alimentador"
    id = Column("id", Integer, primary_key=True)
    matrizId = Column("matrizId", Integer, ForeignKey("matrizes.id"))
    confinamentoId = Column("confinamentoId", Integer,
                            ForeignKey("confinamentos.id"))
    planoId = Column("planoId", Integer, ForeignKey("planos.id"))
    dataEntrada = Column("dataEntrada", DateTime)
    quantidade = Column("quantidade", Integer)
    hash = Column("hash", String)

    matriz = relationship("Matriz", foreign_keys=matrizId)
    confinamento = relationship("Confinamento", foreign_keys=confinamentoId)
    plano = relationship("Plano", foreign_keys=planoId)
