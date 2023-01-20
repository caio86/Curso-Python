# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

import os
clear = lambda: os.system('cls')
clear()
while True:
  numero = input('Digite um número de 0 a 9999: ')
  if len(numero) >= 5 or int(numero) < 0:
    clear()
    print('Erro: número inválido')
  else:
    break

print('Unidade:', numero[-1])
print('Dezena:', numero[-2])
print('Centena:', numero[-3])
print('Milhar:', numero[-4])
