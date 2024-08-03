##Desenvolva um programa que pergunte a distância de uma viagem em Km.##
##Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km e R$0,45 para viagens mais longas.##

distancia = int(input('Qual a distancia da viagem...:'))
valor1 = distancia * 0.50
valor2 = distancia * 0.45
if distancia <= 200:
    print('Você está prestes a começar uma viagem de {:.1f}\nE o preço da sua viagem será de R${}'.format(distancia, valor1 ))
else:
    print('Você está prestes a começar uma viagem de {:.1f}\nE o preço da sua viagem será de R${}'.format(distancia, valor2 ))