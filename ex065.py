r = 'S'
n = count = s = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = input('Quer continuar?[S/N]: ').strip().upper()[0]
    count += 1
    s += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print('Você digitou {} números e a média entre eles é {:.2f}'.format(count , s / count))
print('O maior número é {} e o menor número é {}'.format(maior , menor))
