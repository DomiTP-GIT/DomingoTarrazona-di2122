#!/usr/bin/env python3
"""
Activitat 10
Definix una llista i utilitzant filter, que la separe en dues llistes, una amb els elements parells i l’altra
amb els senars.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def comprobarPar(numero):
	if numero % 2 == 0:
		return True
	return False


def comprobarImpar(numero):
	if numero % 2 == 1:
		return True
	return False


pares = filter(comprobarPar, lista)
impares = filter(comprobarImpar, lista)

pares = list(pares)
impares = list(impares)

print('Pares: \n', pares)
print('Impares\n', impares)
