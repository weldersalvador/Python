from math import hypot
co = float(input('Digite a medida do cateto oposto de um triângulo retângulo em metros: '))
ca = float(input('Digite a medida do cateto adjacente de triângulo retângulo em metros: '))
h = hypot(co,ca)
print('O valor da hipotenusa desse triângulo retângulo vale {:.3f}'.format(h))