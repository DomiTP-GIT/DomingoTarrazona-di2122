#!/usr/bin/env python3

"""
Activitat 11 Crea una aplicació que vaja llegint operacions d’un fitxer (una operació per línia) i
afegisca els resultats. Per exemple, si llig: 4 + 4
Haurà de generar: 4 + 4 = 8
Utilitza funcions anònimes per a implementar les operacions.
"""

import os

operaciones = os.path.join(os.path.dirname(__file__), "operaciones.txt")
resultado = os.path.join(os.path.dirname(__file__), "resultados.txt")

suma = lambda n1, n2: n1 + n2
resta = lambda n1, n2: n1 - n2
multi = lambda n1, n2: n1 * n2
divi = lambda n1, n2: n1 / n2


def leer(archivo):
	lineas = []
	with open(archivo, 'r') as f:
		for linea in f:
			operacion = linea.split(" ")
			num1 = int(operacion[0])
			num2 = int(operacion[2])
			if operacion[1] == "+":
				op = suma(num1, num2)
			elif operacion[1] == "-":
				op = resta(num1, num2)
			elif operacion[1] == "*":
				op = multi(num1, num2)
			elif operacion[1] == "/":
				op = divi(num1, num2)
			add = str(str(operacion[0]) + " " + str(operacion[1]) + " " + str(operacion[2].replace("\n", " ")) + "= " + str(
				op) + "\n")
			lineas.append(add)
		f.close()
	saveFile(lineas)


def saveFile(lineas):
	with open(resultado, 'w') as fi:
		fi.writelines(lineas)


leer(operaciones)
