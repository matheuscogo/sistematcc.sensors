from sqlalchemy import Column, Integer, Boolean, VARCHAR
from ext.db import db

class Matriz(db):
    __tablename__ = 'matrizes'
    # __table_args__ = {"schema":"public"}
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    rfid = Column("rfid", VARCHAR)
    numero = Column("numero", VARCHAR)
    ciclos = Column("ciclos", Integer)
    deleted = Column("deleted", Boolean, default=False)

