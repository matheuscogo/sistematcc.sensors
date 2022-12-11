from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from ext.db import db


class Aviso(db):
    __tablename__ = "avisos"
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    confinamentoId = Column("confinamentos_id", Integer,
                            ForeignKey("confinamentos.id"))
    dataAviso = Column("data_aviso", DateTime)
    separate = Column("separate", Boolean, default=False)
    tipo = Column("tipo", Integer)
    deleted = Column("deleted", Boolean, default=True)
    active = Column("active", Boolean, default=True)
