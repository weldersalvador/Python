from sys import exit
from random import randint
count = 0

print('=' * 60)
print('Irei escolher um número inteiro de 0 a 10, tente acerta-lo')
print('=' * 60)

n = int(input('Digite um número inteiro de 0 a 10: '))
r = randint(0 , 10)
if n == r:
    print('VOCÊ ACERTOU DE PRIMEIRA!!')
while n != r:
    count += 1
    if n > r:
        n = int(input('Menos...tente novamente: '))
    elif n < r:
        n = int(input('Mais...tente novamente: '))
print('Você adivinhou!!! Você precisou de {} tentativas para acertar'.format(count + 1))



