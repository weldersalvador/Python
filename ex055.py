maior = 0
menor = 0
for c in range(1 , 6):
    p = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso foi {} e o menor peso foi {}'.format(maior, menor))