# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

print('-='*20)
print('Conversor de Bases Numéricas')
print('-='*20)
numero = int(input('Digite um número inteiro: '))

while (True):
  print('\n[1] binário')
  print('[2] octal')
  print('[3] hexadecimal')

  escolha = int(input('\nPara qual base você deseja converter? '))

  if escolha == 1:
    nConvertido = bin(numero)
    print(f'A conversão do número {numero} para a base binária é igual a: {nConvertido}')
    break
  elif escolha == 2:
    nConvertido = oct(numero)
    print(f'A conversão do número {numero} para a base octal é igual a: {nConvertido}')
    break
  elif escolha == 3:
    nConvertido = hex(numero)
    print(f'A conversão do número {numero} para a base hexadecimal é igual a: {nConvertido}')
    break
  else:
    print('Escolha inválida.\nTente novamente.')