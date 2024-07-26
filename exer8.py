med = float(input('uma medida em metros?'))
km = med/1000
hm = med/100
dam = med/10
dm = med * 10
cm = med * 100
mm = med * 1000
print('A medida de {:.1f}m corresponde a:'.format(med))
print('{:.3f}km\n''{:.2f}hm\n''{:.1f}dam\n''{:.0f}dm\n''{:.0f}cm\n''{:.0f}mm'.format(km,hm,dam,dm,cm,mm))


