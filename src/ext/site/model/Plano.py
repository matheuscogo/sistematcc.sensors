from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ...db import db


class Plano(db):
    __tablename__ = "planos"
    __table_args__ = {'extend_existing': True}
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String)
    descricao = Column("descricao", String)
    tipo = Column("tipo", String)
    quantidadeDias = Column("quantidadeDias", Integer)
    deleted = Column("deleted", Boolean, default=False)
    active = Column("active", Boolean, default=True)
