#!/usr/bin/env python3
"""
Activitat 8 Fes una aplicació que imprimisca els primers 100 números imparells.
"""
def num_imp():
  cont = 0
  for i in range(0, 1000):
    if cont == 100:
      return
    if i % 2 == 1:
      print(i)
      cont += 1


num_imp()
