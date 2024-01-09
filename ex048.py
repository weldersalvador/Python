s = 0
cont = 0
for c in range(1 , 501 , 2):
    if c % 3 ==0:
        cont = cont + 1
        s += c

print('O somatório dos valores multiplos de 3 entre 1 e 500 é {}'.format(s))
print('Foram somados {} números'.format(cont))
