def area(a , b):
    area = a * b
    print(f'A área de um terreno {a}x{b} é {area}m2')


print('---- CONTROLE DE TERRENOS ----')
a = float(input('Digite o comprimento da parede: '))
b = float(input('Digite a largura da parede: '))
area(a , b)