from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ...db import db


class Registro(db):
    __tablename__ = "registros"
    id = Column("id", Integer, primary_key=True)
    matrizId = Column(Integer, ForeignKey("confinamento.matrizId"))
    dataEntrada = Column("dataEntrada", DateTime)
    dataSaida = Column("dataSaida", DateTime)
    tempo = Column("tempo", DateTime)
    quantidade = Column("quantidade", Integer)
