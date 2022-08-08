from sqlalchemy import Column, Integer, String, Boolean
from ext.db import db


class Matriz(db):
    __tablename__ = "matrizes"
    __table_args__ = {'extend_existing': True}
    id = Column("id", Integer, primary_key=True)
    rfid = Column("rfid", String)
    numero = Column("numero", String)
    ciclos = Column("ciclos", Integer)
    deleted = Column("deleted", Boolean, default=False)
