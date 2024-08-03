##Faça um programa que leia três números e mostre qual é o maios e qual é o menor.##
num1 = int(input('Primeiro numero...:'))
num2 = int(input('Segundo numero...:'))
num3 = int(input('Terceiro numero...:'))

menor = num1
maior = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3< num1 and num3 < num2:
    menor = num3
if num2 > num1 and num2 > num3:
    maior = num2 
if num3 > num1 and num3 > num2:
    maior = num3

print('O menor numero foi {}\nO maior numero foi {}'.format(menor,maior))