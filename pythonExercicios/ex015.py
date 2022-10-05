diasAlugados = int(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos Km rodados? '))
totalPagar = diasAlugados * 60 + kmRodados * 0.15
print('O total a pagar é de R${:.2f}'.format(totalPagar))
