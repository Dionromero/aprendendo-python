salario = float(input('Qual e o salario do funcionario...: R$ '))
porcentagem = float(input('Qual e a porcentagem do aumento...:'))
aumento = salario + (salario * porcentagem/100)

print('um funcionario que ganhava R$ {} , com aumento de {}% , passa a receber R${:.2f} .'.format(salario, porcentagem, aumento))