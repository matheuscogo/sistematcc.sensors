from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from ext.db import db


class Inseminacao(db):
    __tablename__ = "inseminacoes"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    planoId = Column("planos_id", Integer, ForeignKey("planos.id"))
    matrizId = Column("matriz_id", Integer, ForeignKey("matrizes.id"))
    confinamentoId = Column("confinamentos_id", Integer,
                            ForeignKey("confinamentos.id"))
    dataInseminacao = Column("data_inseminacao", DateTime)
    active = Column("active", Boolean, default=True)
    deleted = Column("deleted", Boolean, default=False)
