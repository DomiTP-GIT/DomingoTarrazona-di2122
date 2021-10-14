#!/usr/bin/env python3
"""
Activitat 12 Modifica el codi de l’activitat 11 per a que no es produïsquen errors en l’execució, ja siga
per introdïur valor no definits per a lesfuncions, valors que no són numèrics o operacions desconegudes.
Controla també que no es produïsquen errors en la lectura/escriptura dels arxius
"""
import os

operaciones = os.path.join(os.path.dirname(__file__), "operaciones.txt")
resultado = os.path.join(os.path.dirname(__file__), "resultados.txt")

suma = lambda n1, n2: n1 + n2
resta = lambda n1, n2: n1 - n2
multi = lambda n1, n2: n1 * n2
divi = lambda n1, n2: n1 / n2


def leer(archivo):
	try:
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
	except ZeroDivisionError:
		print("No puedes dividir un número entre cero")
	except ArithmeticError:
		print("Error en las operaciones")
	except TypeError:
		print("Error en el tipo")


def saveFile(lineas):
	try:
		with open(resultado, 'w') as fi:
			fi.writelines(lineas)
	except (FileNotFoundError, IOError):
		print("Error con los ficheros")
	finally:
		fi.close()


leer(operaciones)
