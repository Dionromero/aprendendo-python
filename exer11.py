largura = float(input('Largura da parede...:'))
altura = float(input('Altura da parede...:'))
area = largura * altura
tinta = area/2 
print('Sua parede tem dimensao {:.1f} X {:.1f} e sua area e de {:.1f}m².\n' 'Para pintar essa parede, voce precisara de {}l de tinta.'.format(largura, altura, area,tinta))