dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
diasp = (dias * 60) + (km * 0.15)
print('total a pagar é de R${:.2f}'.format(diasp))