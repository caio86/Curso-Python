# Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

triangulo = False
tipo = ''

if (n1 >= n2) & (n1 >= n3):
  triangulo = (n2 + n3) > n1
elif (n2 >= n1) & (n2 >= n3):
  triangulo = (n1 + n3) > n2
else:
  triangulo = (n1 + n2) > n3

if n1 == n2 == n3:
  tipo = "Equilátero"
elif (n1 == n2) or (n2 == n3) or (n1 == n3):
  tipo = "Isósceles"
else:
  tipo = "Escaleno"

print('Os números {}, {} e {} {} um triângulo{}'.format(n1, n2, n3, 'formam' if triangulo else 'não formam', (" " + tipo) if triangulo else ''))