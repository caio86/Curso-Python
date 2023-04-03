# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('Calculo da média escolar')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
status = ""

if media >= 7:
  status = "APROVADO"
elif media >= 5:
  status = "EM RECUPERAÇÃO"
else:
  status = "REPROVADO"

print(f'A sua média foi de {media:.1f} e você está: {status}')

