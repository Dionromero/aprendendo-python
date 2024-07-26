real = float(input('Quanto dinheiro tem na sua carteira...: R$'))
dolar = 5.59
valor = real / dolar
print('Com R${:.2f} voce pode comprar U${:.2f}'.format(real, valor))