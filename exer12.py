produto = float(input('Qual o preço do produto...: R$'))
porcentagem = float(input('Qual a porcentagem do desconto...:'))
valor = produto - (produto * porcentagem /100)

print('O produto que custava R${} ,na promoção com desconto de {}% vai custar R${:.2f}'.format(produto, porcentagem, valor))
    