# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
antigoSalario = float(input('Digite o salário do funcionário: R$'))
novoSalario = antigoSalario + (antigoSalario * 15) / 100
print('O funcionário recebeu um aumento de 15% e agora está com um salário de R${}'.format(novoSalario))
