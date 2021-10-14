#!/usr/bin/env python3
"""
Activitat 13 Anem a implementar un xicotet joc per consola. El programa generarà un número
aleatori entre 0 i 100 (utilitzeu randint() del mòdul random) i demanarà a l’usuari que introduïsca un
número.
Mentre el número siga massa menut, llançarà una excepció ErrorEnterMassaMenut indicant-li-ho. Si
per contra és massa gran llançarà ErrorEnterMassaGran.
El joc acabarà quan s’introduïsca un valor no numèric o quan s’introduïsca l’enter buscat, en este cas
felicitarà a l’usuari.
"""
import random


class ErrorEnterMassaMenut(Exception):
	pass


class ErrorEnterMassaGran(Exception):
	pass


aleatorio = random.randint(0, 100)
while True:
	numero = input("Introduce un numero: ")
	try:
		numero = int(numero)
		if numero == aleatorio:
			print("Has acertado el numero")
			break
		elif numero < aleatorio:
			raise ErrorEnterMassaMenut
		elif numero > aleatorio:
			raise ErrorEnterMassaGran
	except ErrorEnterMassaMenut:
		print("El numero es massa menut")
	except ErrorEnterMassaGran:
		print("El numero es massa gran")
	except ValueError:
		print("Saliendo, valor no numérico")
		break
