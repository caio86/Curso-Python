# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do sue aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
  novoSalario = salario + (salario * 0.1)
else:
  novoSalario = salario + (salario * 0.15)

print('O novo valor do salário será de R${:.2f}'.format(novoSalario))
