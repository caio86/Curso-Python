# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint

pcJogada = "pedra"
jogada = "pedra"
status = ""

match randint(1,3):
  case 1:
    pcJogada = "pedra"
  case 2:
    pcJogada = "papel"
  case 3:
    pcJogada = "tesoura"

print('Pedra Papel e Tesoura')
escolha = int(input("""
[1] - Para Pedra
[2] - Para Papel
[3] - Para Tesoura
Escolha a sua Jogada: """))

match escolha:
  case 1:
    jogada = "pedra"
    if pcJogada == "papel": status = "VOCÊ PERDEU"
    if pcJogada == "tesoura": status = "VOCÊ GANHOU"
    if pcJogada == "pedra": status = "EMPATE"
  case 2:
    jogada = "papel"
    if pcJogada == "tesoura": status = "VOCÊ PERDEU"
    if pcJogada == "pedra": status = "VOCÊ GANHOU"
    if pcJogada == "papel": status = "EMPATE"
  case 3:
    jogada = "tesoura"
    if pcJogada == "pedra": status = "VOCÊ PERDEU"
    if pcJogada == "papel": status = "VOCÊ GANHOU"
    if pcJogada == "tesoura": status = "EMPATE"

print(status)
print(f'Você escolheu {jogada} e o computador escolheu {pcJogada}')
