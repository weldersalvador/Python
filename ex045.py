import sys
from sys import exit
from time import sleep
from random import randint

l = ['Pedra', 'Papel', 'Tesoura']
print('Escolha [0] para Pedra')
print('Escolha [1] para Papel')
print('Escolha [2] para Tesoura')
e = int(input('Faça sua escolha: '))
c = randint(0 , 2)
if e > 2:
    print('Comando inválido! Por favor, reinicie o programa.')
    sys.exit()
print('JO')
sleep(0.65)
print('KEN')
sleep(0.65)
print('PÔ!!')
print('-=' * 14)
print('O computador escolheu {}'.format(l[c]))
print('O jogador escolheu {}'.format(l[e]))
print('-=' * 14)
if c == 0:
    if e == 0:
        print('EMPATE!')
    elif e == 1:
        print('O JOGADOR GANHOU!')
    elif e == 2:
        print('O COMPUTADOR GANHOU!')
elif c == 1:
    if e == 0:
        print('O COMPUTADOR GANHOU!')
    elif e == 1:
        print('EMPATE!')
    elif e == 2:
        print('O JOGADOR GANHOU!')
elif c == 2:
    if e == 0:
        print('O JOGADOR GANHOU!')
    elif e == 1:
        print('O COMPUTADOR GANHOU!')
    elif e == 2:
        print('EMPATE!')







