import random
from time import sleep

print('=' * 60)
print('Irei escolher um número inteiro de 0 a 5, tente acerta-lo')
print('=' * 60)
n = int(input('Escolha um número: '))
r = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('O numero escolhido foi {}'.format(r))
if n == r:
    print('Parabéns! Você acertou!')
else:
    print('Você errou!')
