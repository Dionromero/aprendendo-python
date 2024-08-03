##Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.##
##Para salários superiores a R$1250,0, calcule um aumento de 10%.Para os inferiores ou iguais, o aumento é de 15%.##

salario = float(input('Qual e o salario do funcionario...:'))
aumento = salario + (salario * 15/100)
aumento2 = salario + (salario * 10/100)
if salario <= 1250.0:
    print('Quem ganhva R${}, passa a ganhar R${}'.format(salario, aumento))
else:
    print('Quem ganhava R${}, passa a ganhar R${}'.format(salario, aumento2))
