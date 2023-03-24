# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar.
# - se é a hora de se alistar.
# - se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo

from datetime import datetime

ano = int(input('Qual o ano que você nasceu? '))
anoAtual = datetime.now().year
timeDiff = anoAtual - ano

if timeDiff > 18:
  print('Já passou do tempo do seu alistamento')
  print(f'O seu tempo de alistamento foi há {timeDiff-18} anos atrás')
elif timeDiff == 18:
  print('Esse é o ano de se alistar')
else:
  print('Ainda não chegou o tempo do seu alistamento')
  print(f'O seu tempo de alistamento será daqui há {timeDiff-18} anos')