n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número é maior!'.format(n1 , n2))
elif n2 > n1:
    print('O segundo número é maior!'.format(n2 , n1))
else:
    print('Esses números são iguais!')