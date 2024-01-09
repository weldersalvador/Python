from random import choice , randint
lista = ['Impar' , 'Par']
random = choice(lista)
random2 = randint(0, 10)
count = 0
while True:
    número = int(input('Digite um número: '))
    impar_par = str(input('Você quer ímpar ou par? [I/P]: ')).strip().upper()[0]
    while not impar_par in 'IiPp':
        impar_par = str(input('Você quer ímpar ou par? [I/P]: ')).strip().upper()[0]
    if impar_par == 'I':
        print('Você jogou {} e o computador jogou {}, totalizando {}'.format(número , random2, número + random2),end=' ')
        if (número + random2) % 2 == 0:
            print('que é par')
        else:
            print('que é impar')
        if (random2 + número) % 2 == 0:
            print('Você perdeu!!')
            print('Você ganhou um total de {} vezes'.format(count))
            break
        if (random2 + número) % 2 == 1:
            print('Você ganhou!!')
            count += 1
    if impar_par == 'P':
        print('Você jogou {} e o computador jogou {}, totalizando {}'.format(número, random2, número + random2), end=' ')
        if (número + random2) % 2 == 0:
            print('que é par')
        else:
            print('que é impar')
        if (número + random2) % 2 == 0:
            print('Você ganhou!!')
            count += 1
        if (random2 + número) % 2 == 1:
            print('Você perdeu!')
            print('Você ganhou um total de {} vezes'.format(count))
            break
print('FIM')