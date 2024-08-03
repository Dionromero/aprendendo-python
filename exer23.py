##Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.##
##O programa devera escrever na tela se o usuário venceu ou perdeu##

import random

num = random.randrange(0,5)
acertei = int(input('Tente acertar o numero escolhido...:'))

if num == acertei:
    print('PARABENS!!!! voce acertou o numero\nNUmero escolhido por voce...: {}\nNumero escolhido pelo programa...: {}'.format(acertei, num))
else:
    print('INFELIZMENTE, voce errou o numero\nNumero escolhido por voce...: {}\nNumero escolhido pelo programa...: {}'.format(acertei, num))