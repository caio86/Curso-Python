# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

msg = input('Digite qualquer coisa: ')

# testar float
if msg.isdecimal():
  print('O valor é um número')
else:
  print('O valor é uma string')
  if msg.isupper():
    print('A String está em maiúscula')
  else:
    print('A String está em minúscula')
  if msg.isalpha():
    print('A String não possui números')
  else:
    print('A String possui números')
