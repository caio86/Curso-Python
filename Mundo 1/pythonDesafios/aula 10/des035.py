# Desenvolva um programa que leia o comprimento de três retas e diga ao usurário se elas podem ou não formar um triângulo.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

triangulo = False

if (n1 >= n2) & (n1 >= n3):
  triangulo = (n2 + n3) > n1

if (n2 >= n1) & (n2 >= n3):
  triangulo = (n1 + n3) > n2

if (n3 >= n1) & (n3 >= n2):
  triangulo = (n1 + n2) > n3

print(n2>=n1)
print(n2>=n3)
print(n2>=n3 & n2>=n1)

print('Os números {}, {} e {} {} um triângulo'.format(n1, n2, n3, 'formam' if triangulo else 'não formam'))