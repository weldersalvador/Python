soma = 0
maior = 0
menor = 0
count = 0
for c in range(1 , 5):
    n = input('Digite o nome da {} pessoa: '.format(c))
    i = int(input('Idade: '))
    s = input('Sexo (M/F): ')
    soma += i
    if c == 1 and s in 'Mm':
        maior = n
        menor = n
    else:
        if c > i and s in 'Mm':
            maior = n
        if c < i and s in 'Mm':
            menor = n

    if i < 20 and s == 'F':
        count += 1

print('A média das idades é {}'.format(soma / 4))
print('O homem que possui a maior idade é {}'.format(maior))
print('{} mulheres tem menos de 20 anos'.format(count))

