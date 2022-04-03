from ...db import db

class Usuario(db.Model):
    __tablename__ = "logs"
    id = db.Column("id", db.Integer, primary_key=True)
    matrizRfid = db.Column("email", db.Unicode, unique=True, nullable=False)
    acao = db.Column("senha", db.Unicode)
    admin = db.Column("admin", db.Boolean)















#
# class Usuario():
#
#     ...
#     # def inserirMatriz(self):  # Create
#     #     try:
#     #         conn.cursor().execute("INSERT INTO matrizes (rfid, quantidade) VALUES (%s, %s)", (rfid, quantidade))
#     #         conn.commit()
#     #         return True
#     #     except Exception as e:
#     #         return False
#     #
#     # def consultarMatriz(self):  # Read
#     #     try:
#     #         result = conn.cursor()
#     #         result.execute('SELECT * FROM matrizes')
#     #         rows = result.fetchall()
#     #         return rows
#     #     except Exception as e:
#     #         return "Erro ao consultar a base de dados! " + str(e)
#     #
#     # def consultarMatrizes(self):  # Read
#     #     try:
#     #         rfid = rasp.leitorRFID()
#     #         result = conn.cursor()
#     #         result.execute('SELECT * FROM matrizes WHERE rfid = (%s)', (rfid))
#     #         rows = result.fetchall()
#     #         cont = 0
#     #         return rows
#     #     except Exception as e:
#     #         return "Erro ao consultar registros da base de dados! " + str(e)
#     #
#     # def atualizarMatriz(self):  # Update
#     #     try:
#     #         result = conn.cursor()
#     #         result.execute('UPDATE matrizes SET quantidade = WHERE = ')
#     #         rows = result.fetchall()
#     #         return rows
#     #     except Exception as e:
#     #         return "Erro ao consultar a base de dados! " + str(e)
#     #
#     # def excluirMatriz(self):  # Delete
#     #     try:
#     #         result = conn.cursor()
#     #         result.execute('DELETE FROM matrizes WHERE rfid =')
#     #         rows = result.fetchall()
#     #         return rows
#     #     except Exception as e:
#     #         return "Erro ao consultar a base de dados! " + str(e)