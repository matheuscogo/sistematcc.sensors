from sqlalchemy import Column, Integer, VARCHAR, Boolean
from ext.db import db


class Matriz(db):
    __tablename__ = "matrizes"
    id = Column("id", Integer, primary_key=True)
    rfid = Column("rfid", VARCHAR)
    numero = Column("numero", VARCHAR)
    ciclos = Column("ciclos", Integer)
    deleted = Column("deleted", Boolean, default=False)
