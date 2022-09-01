# Crie um programa que leia dois números e mostre a soma entre eles.
n1 = input('Digite o primeiro número:  ')
n2 = input('Digite o segundo número:  ')

if n1.isdecimal():
  n1 = int(n1)
else:
  n1 = float(n1)

if n2.isdecimal():
  n2 = int(n1)
else:
  n2 = float(n1)

s = n1 + n2

print('A soma de {} e {} vale {}'.format(n1, n2, s))
