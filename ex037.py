n = int(input('Escolha um número inteiro: '))
m = int(input('Digite 0 para conversão binária, 1 para conversão octal e 2 para conversão hexadecimal: '))
if m == 0:
    print('O número {} convertido para binário será {}.'.format(n,bin(n)[2:]))
elif m == 1:
    print('O número {} convertido para octal será {}'.format(n,oct(n)[2:]))
elif m == 2:
    print('O número {} convertdio para hexadecimal será {}'.format(n,hex(n)[2:]))
else:
    print('Só os q eu pedi carai')
