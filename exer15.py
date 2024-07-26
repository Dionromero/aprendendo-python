dias = int(input('Quantos dias com o carro...:'))
km = float(input('Quantos km rodados...:'))
diaria = (dias * 60) + (km * 0.15)

print('O total a pagar e de R$ {} '.format(diaria))