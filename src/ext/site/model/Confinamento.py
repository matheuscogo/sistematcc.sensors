from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from ext.db import db

class Confinamento(db):
    __tablename__ = "confinamentos"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    planoId = Column("plano_id", Integer, ForeignKey('planos.id'))
    matrizId = Column("matriz_id", Integer, ForeignKey('matrizes.id'))
    dataConfinamento = Column("data_confinamento", DateTime)
    active = Column("active", Boolean, default=True)
    deleted = Column("deleted", Boolean, default=True)
    
