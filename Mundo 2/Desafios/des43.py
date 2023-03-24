# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('Calculo do IMC')
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
status = ''
imc = peso / altura**2

if imc > 40:
  status = 'Obesidade Mórbida'
elif imc >= 30:
  status = 'Obesidade'
elif imc >= 25:
  status = 'Sobrepeso'
elif imc >= 18.5:
  status = 'Peso ideal'
else:
  status = 'Abaixo do Peso'

print(f'O seu IMC é {imc:.2f}, oque equivale a um status de {status}')