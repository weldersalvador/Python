from sys import exit
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um outro número: '))
print('[1] SOMA ')
print('[2] MULTIPLICAÇÃO')
print('[3] MAIOR')
print('[4] NOVOS NÚMEROS')
print('[5] SAIR DO PROGRAMA')
n3 = int(input(': ').strip())
if n3 == 0 or n3 > 5:
    print('Comando inválido! Por favor, comece novamente.')
    exit()
elif n3 == 1:
    print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
elif n3 == 2:
    print('A multiplicação entre {} e {} é {}'.format(n1 , n2 , n1 * n2))
elif n3 == 3:
    if n1 > n2:
        print('O maior número é {} e o menor número é {}'.format(n1 , n2))
    else:
        print('O maior número é {} e o menor é {}'.format(n2, n1))
elif n3 == 4:
    while not n3 != 4:
        n4 = n1 = float(input('Digite um número: '))
        n5 = n2 = float(input('Digite um outro número: '))
        print('[1] SOMA ')
        print('[2] MULTIPLICAÇÃO')
        print('[3] MAIOR')
        print('[4] NOVOS NÚMEROS')
        print('[5] SAIR DO PROGRAMA')
        n6 = n3 = int(input(': '))
        if n3 == 1:
            print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        elif n3 == 2:
            print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
        elif n3 == 3:
            if n1 > n2:
                print('O maior número é {} e o menor número é {}'.format(n1, n2))
            else:
                print('O maior número é {} e o menor é {}'.format(n2, n1))
elif n3 == 5:
    exit()

while n3 != 5:

    print('[1] SOMA ')
    print('[2] MULTIPLICAÇÃO')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    n3 = int(input(': ').strip())
    if n3 == 0 or n3 > 5:
        print('Comando inválido! Por favor, comece novamente.')
        exit()
    elif n3 == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif n3 == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif n3 == 3:
        if n1 > n2:
            print('O maior número é {} e o menor número é {}'.format(n1, n2))
        else:
            print('O maior número é {} e o menor é {}'.format(n2, n1))
    elif n3 == 4:
        while not n3 != 4:
            n4 = n1 = float(input('Digite um número: '))
            n5 = n2 = float(input('Digite um outro número: '))
            print('[1] SOMA ')
            print('[2] MULTIPLICAÇÃO')
            print('[3] MAIOR')
            print('[4] NOVOS NÚMEROS')
            print('[5] SAIR DO PROGRAMA')
            n6 = n3 = int(input(': '))
            if n3 == 1:
                print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
            elif n3 == 2:
                print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
            elif n3 == 3:
                if n1 > n2:
                    print('O maior número é {} e o menor número é {}'.format(n1, n2))
                else:
                    print('O maior número é {} e o menor é {}'.format(n2, n1))







