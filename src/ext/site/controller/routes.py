# from ...db import matrizCRUD, registroCRUD, confinamentoCRUD
# import datetime
# import time
# from ..model.Registro import Registro

# bot1 = 37
# bot2 = 35
# led1 = 40
# led2 = 38
# led3 = 36

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(bot1, GPIO.IN)
# GPIO.setup(bot2, GPIO.IN)
# GPIO.setup(led1, GPIO.OUT)
# GPIO.setup(led2, GPIO.OUT)
# GPIO.setup(led3, GPIO.OUT)

# dataEntrada = ""
# horaEntrada = ""
# matriz = 0
# quantidade = 0
# dataSaida = ""
# horaSaida = ""

# while True:
# 	uid = rasp.leitorRFID()
# 	 entrada = 1
# 	  while entrada:
# 		   if not matrizCRUD.existsRFID(str(uid)):
# 				print('Matriz {} identificada'.format(uid))
# 				dataEntrada = str(datetime.datetime.now().strftime("%Y-%m-%d"))
# 				horaEntrada = datetime.datetime.now()
# 				# matriz = matrizCRUD.consultarMatrizID(str(uid))
# 				GPIO.output(led3, 1)
# 				time.sleep(1)
# 				GPIO.output(led3, 0)
# 				numero = 0
# 				alimentador = 1
# 				while alimentador:
# 					if (GPIO.input(bot1) == 1):
# 						print('Matriz {} solicitou alimento'.format(uid))
# 						quanti = confinamentoCRUD.consultarQuantidade(
# 							str(uid), dataEntrada)
# 						print("----------")
# 						print()
# 						print("Quanti = " + str(quanti))
# 						print("Quantidade = " + str(quantidade))
# 						print()
# 						print("----------")
# 						if quanti > quantidade:
# 							numero = numero + 1
# 							quantidade = quantidade + 400
# 							GPIO.output(led2, 1)
# 							print(str(time.sleep(5).__str__))
# 							GPIO.output(led2, 0)
# 							alimentador = 1
# 					if (GPIO.input(bot2) == 1):
# 						GPIO.output(led1, 1)
# 						time.sleep(1)
# 						GPIO.output(led1, 0)
# 						dataSaida = str(
# 							datetime.datetime.now().strftime("%Y-%m-%d"))
# 						horaSaida = datetime.datetime.now()
# 						tempo = str(horaSaida - horaEntrada)
# 						horaEntrada = str(horaEntrada.strftime("%H:%M:%S"))
# 						horaSaida = str(horaSaida.strftime("%H:%M:%S"))
# 						registro = Registro(matriz=matriz, dataEntrada=dataEntrada, dataSaida=dataSaida,
# 											horaEntrada=horaEntrada, horaSaida=horaSaida, tempo=tempo, quantidade=quantidade)
# 						print("Data de entrada: " + str(dataEntrada) + ", " +
# 							  str(type(dataEntrada)) + ", " + str(type(str(dataEntrada))))
# 						print("Hora de entrada: " + str(horaEntrada) + ", " +
# 							  str(type(horaEntrada)) + ", " + str(type(str(horaEntrada))))
# 						print("ID da matriz:    " + str(matriz) + ", " +
# 							  str(type(matriz)) + ", " + str(type(matriz)))
# 						print("Data de saida:   " + str(dataSaida) + ", " +
# 							  str(type(dataSaida)) + ", " + str(type(str(dataSaida))))
# 						print("Hora de saida:   " + str(horaSaida) + ", " +
# 							  str(type(horaSaida)) + ", " + str(type(str(horaSaida))))
# 						print("Tempo:   " + str(tempo) + ", " +
# 							  str(type(tempo)) + ", " + str(type(str(tempo))))
# 						print("Quantidade:   " + str(quantidade) + ", " +
# 							  str(type(quantidade)) + ", " + str(type(str(quantidade))))
# 						print("Dia:   " + str(quanti) + ", " +
# 							  str(type(quanti)) + ", " + str(type(str(quanti))))
# 						if registroCRUD.cadastrarRegistro(registro):
# 							quantidade = 0
# 							quanti = 0
# 							total = 0
# 							dia = 0
# 							print("Sucesso")
# 						else:
# 							print("Falha")
# 						print('Matriz {} saiu do alimentador'.format(uid))
# 						print('Reiniciando sistema')
# 						alimentador = 0
# 						entrada = 0
# 			else:
# 				print("erro rfid")
