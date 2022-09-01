def definir_tipo(numero):
  numero = str(numero)
  if '.' in numero:
    return float(numero)
  else:
    return int(numero)


n1 = definir_tipo(input('Digite um valor: '))
n2 = definir_tipo(input('Digite outro valor: '))

s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
