print('-=' * 2)
print('PA')
print('-=' * 2)

a1 = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
print('Os 10 primeiros termos dessa PA é:')
for c in range(a1 ,  a1 + 10 * r , r):

    print(c , end=' ')