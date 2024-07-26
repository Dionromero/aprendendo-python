num = int(input('Digite um numero...:'))
numdobro = num * 2 
numtri = num * 3 
numraiz = num ** (1/2)

print('Numero:{:^5}\n' 'O dobro do numero:{:^5}\n' 'O triplo do numero:{:^5}\n' 'A raiz do numero: {:^5.2f}\n'.format(num, numdobro, numtri, numraiz))