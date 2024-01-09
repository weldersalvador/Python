d = input('Digite uma frase: ').strip().replace(' ', '')
rev = ''.join(reversed(d))
print('O inverso de {} é {}'.format(d.upper() , rev.upper()))
if rev == ''.join(reversed(rev)):
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
