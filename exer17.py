import math 

#seno = float(input('Comprimento do cateto oposto...:'))
#cos = float(input('comprimento do cateto adjacente...:')) 
#hipo = (seno ** 2  + cos ** 2) ** (1/2)

#print('A hipotenusa vai medir {:.2f}'.format(hipo))



seno = float(input('Comprimento do cateto oposto...:'))
cos = float(input('Comprimento do cateto adjacente...:'))

hipo = math.hypot(seno,cos)

print('O valor da hipotenusa e...: {:.2f}'.format(hipo))