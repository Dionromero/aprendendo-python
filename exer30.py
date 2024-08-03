##Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.##
seg1 = float(input('Primeiro segmento...:'))
seg2 = float(input('Segundo segmento...:'))
seg3 = float(input('Terceiro segmento...:'))

print('=' * 25)
print('ANALISADOR DE TRIÂNGULOS')
print('=' * 25)

if seg2 + seg3 > seg1 and seg1 + seg3 > seg2 and seg1 + seg2 > seg3:
    print('Primeiro segmento...: {}\nSegundo segmento...: {}\nTerceiro segmento...: {}\nOs segmentos acima podem formar um triângulo.'.format(seg1,seg2,seg3))
else:
    print('Os segmentos acima não podem forma um triângulo')