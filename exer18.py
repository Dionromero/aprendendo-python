import math

ang = float(input('Digite o angulo que deseja...:'))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}\n''O angulo de {} tem o COSSENO de {:.2f}\n''O angulo de {} tem TANGENTE de {:.2f}'.format(ang,seno,ang,cos,ang,tan))