# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27
real = float(input('Quantos reais você tem? R$'))
dolar = real / 3.27
print('Com R${:.2f} é possível comprar US${:.2f}'.format(real, dolar))
