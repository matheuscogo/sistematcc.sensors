# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
# from ...db import db


# class Aviso(db):
#     __tablename__ = "avisos"
#     id = Column("id", Integer, primary_key=True)
#     confinamentoId = Column(Integer, ForeignKey("confinamento.id"))
#     dataAviso = Column("dataAviso", DateTime)
#     separar = Column("separar", Boolean, default=False)
#     active = Column("active", Boolean, default=True)
