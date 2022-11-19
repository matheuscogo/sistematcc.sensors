from sqlalchemy import Column, Integer, Boolean, VARCHAR
from ext.db import db

class Plano(db):
    __tablename__ = 'planos'
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", VARCHAR)
    descricao = Column("descricao", VARCHAR)
    tipo = Column("tipo", VARCHAR)
    quantidadeDias = Column("quantidade_dias", Integer)
    deleted = Column("deleted", Boolean, default=False)
    active = Column("active", Boolean, default=True)
