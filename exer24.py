##Escreva um programa que leia a velocidade de um carro.##
##Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.##
##A multa vai custar  R$7,00 por cada Km acima do limite.##

velo = int(input(' Qual a velocidade atual do carro...:'))
limite = int(input(' Qual e o limite de velocidade da rua...:'))
multa = (velo - limite) * 7.0


if velo <= limite :
    print(' Tenha um bom dia! dirija com segurança!!')
else:
    print(' Você recebeu uma multa no valor de...: R${}'.format(multa))