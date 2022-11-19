from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ext.db import db

class Registro(db):
    __tablename__ = "registros"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    matrizId = Column("matriz_id", Integer, ForeignKey("matrizes.id"))
    dataEntrada = Column("data_entrada", DateTime)
    dataSaida = Column("data_saida", DateTime)
    quantidade = Column("quantidade", Integer)
