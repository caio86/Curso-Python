# A confederação nacional de natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

# Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import datetime

print('Programa de categorização de atleta')
ano = int(input('Qual o ano que você nasceu? '))
anoAtual = datetime.now().year
timeDiff = anoAtual - ano

if timeDiff > 20:
    status = 'MASTER'
elif timeDiff > 19:
  status = 'SÊNIOR'
elif timeDiff > 14:
  status = 'JUNIOR'
elif timeDiff > 9:
  status = 'INFANTIL'
else:
  status = 'MIRIM'

print(f'Você tem {timeDiff} anos e está na categoria: {status}')
