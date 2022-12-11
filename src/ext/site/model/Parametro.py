from sqlalchemy import Column, Integer
from ext.db import db


class Parametro(db):
    __tablename__ = "parametros"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tempoPorcao = Column("tempo_porcao", Integer)
    quantidadePorcao = Column("quantidade_porcao", Integer)
    intervaloPorcoes = Column("intervalo_porcoes", Integer)
    tempoProximaMatriz = Column("tempo_proxima_matriz", Integer)
    tempoSemBrinco = Column("tempo_sem_brinco", Integer)
