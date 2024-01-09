n1 = float(input('Digite um número: '))
n2 = float(input('Digite um outro número: '))
n3 = float(input('Digite um ultimo número: '))
if n1 > n2 > n3:
    print('O maior número é {} e o menor número é {}'.format(n1,n3))
if n2 >n1> n3:
    print('O maior número é {} e o menor número é {}'.format(n2,n3))
if n2 > n3 > n1:
    print('O maior número é {} e o menor número é {}'.format(n2,n1))
if n1 > n3  > n2:
    print('O maior número é {} e o menor número é {}'.format(n1,n2))
if n3 > n2 > n1:
    print('O maior número é {} e o menor número é {}'.format(n3,n1))
if n3 > n1 > n2:
    print('O maior número é {} e o menor número é {}'.format(n3,n2))
else:
    print('Todos são iguais!')


