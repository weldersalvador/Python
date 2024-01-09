m1 = float(input('Digite o valor da primeira medida: '))
m2 = float(input('Digite o valor da segunda medida: '))
m3 = float(input('Digite o valor da terceira medida: '))
if m1 < m2 + m3 and m2 < m3 + m1 and m3 < m2 + m1:
    print('Você pode formar um triângulo com essas medidas!')
    if m1 == m2 == m3:
        print('Esse triângulo é equilátero! ')
    elif m1 != m2 != m3 and m3 != m1:
        print('Esse triângulo é escaleno!')
    elif m1 == m2 or m1 == m3 or m2 == m3:
        print('Esse triângulo é isosceles!')
else:
    print('Você não pode formar um triângulo com essas medidas!')






