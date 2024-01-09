import math
n = float(input('Digite um ângulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O seno de {:.2f}° vale {:.2} \nO cosseno vale {:.2f} \nA tangente vale {:.2f}'.format(n,s,c,t))