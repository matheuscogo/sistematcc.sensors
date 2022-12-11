from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from ext.db import db

class Parametro(db):
    __tablename__ = "parametros"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tempoPorção = Column("tempoPorção",Integer)
    quantidadePorção = Column("quantidadePorção", Integer)
    intervaloPorções = Column("intervaloPorções", Integer)
    tempoProximaMatriz = Column("tempoProximaMatriz", Integer)

