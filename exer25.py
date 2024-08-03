##Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR##
num = int(input('Digite um numero...:'))

if num % 2 == 0 :
    print('O numero e {} PAR'.format(num))
else:
    print('O numero e {} IMPAR'.format(num))