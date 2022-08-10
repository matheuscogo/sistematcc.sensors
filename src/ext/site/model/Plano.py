from sqlalchemy import Column, Integer, VARCHAR, Boolean
from ext.db import db


class Plano(db):
    __tablename__ = "planos"
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", VARCHAR)
    descricao = Column("descricao", VARCHAR)
    tipo = Column("tipo", VARCHAR)
    quantidadeDias = Column("quantidadeDias", Integer)
    deleted = Column("deleted", Boolean, default=False)
    active = Column("active", Boolean, default=True)
