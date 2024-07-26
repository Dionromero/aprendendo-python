nota1 = int(input('Digite a primeira nota...:'))
nota2 = int(input('Digite a segunda nota...:'))

media = (nota1 + nota2) / 2 

print( 100 * '-')
print('Primeira nota...: {:^}\n' 'Segunda nota...: {:^}\n' 'media...: {:^}'.format(nota1, nota2, media))
print( 100 * '-')