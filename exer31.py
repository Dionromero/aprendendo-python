casa = int(input('Qual o valor da casa...:'))
salario = int(input('qual o salario do cliente...:'))
prestacao = int(input('Quantas prestações...:'))

valor = casa / prestacao

print(f'O valor da prestação é de R$ {valor}')

if valor > salario * 0.3:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado')
    print(f'Valor da casa...: R$ {casa}')
    print(f'Valor do salario...: R$ {salario}')
    print(f'Quantidade de prestações...: {prestacao}')
    print(f'Valor da prestação...: R$ {valor}')
