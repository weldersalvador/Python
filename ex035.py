import math
m1 = float(input('Digite uma medida: '))
m2 = float(input('Digite outra medida: '))
m3 = float(input('Digite uma ultima medida: '))
if m1 < m3 + m2 and m2 < m3 + m1 and m3 < m2 + m1:
    print('Com essas medidas podemos formar um triângulo! ')
else:
    print('Não podemos formar um triângulo com essas medidas.')
