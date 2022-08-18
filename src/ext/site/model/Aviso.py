from email.policy import default
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, VARCHAR
from sqlalchemy.orm import relationship
from ext.db import db


class Aviso(db):
    __tablename__ = "avisos"
    id = Column("id", Integer, primary_key=True)
    confinamentoId = Column(Integer, ForeignKey("confinamentos.id"))
    dataAviso = Column("dataAviso", DateTime)
    separar = Column("separar", Boolean, default=False)
    status = Column("status", Integer)
    active = Column("active", Boolean, default=True)
    sync = Column("sync", VARCHAR, default)
    confinamento = relationship("Confinamento", foreign_keys=confinamentoId)
