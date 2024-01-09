from random import randint
from time import sleep
lista = list()
soma = 0
def sorteio(lista):
    print('SORTEANDO...')
    for count in range(1 , 6):
        n = randint(1, 10)
        print(n , end=' ', flush=True)
        lista.append(n)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares da lista {lista} vale {soma}')


    

sorteio(lista)
somaPar(lista)