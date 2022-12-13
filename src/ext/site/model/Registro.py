from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ext.db import db


class Registro(db):
    __tablename__ = "registros"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    confinamentoId = Column("confinamentos_id", Integer,
                            ForeignKey("confinamentos.id"))
    dataEntrada = Column("data_entrada", DateTime)
    dataSaida = Column("data_saida", DateTime)
    quantidade = Column("quantidade", Integer)
