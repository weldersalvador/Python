from random import randint
numeros = (randint(1, 10), randint(1,10) , randint(1, 10), randint(1, 10), randint(1 , 10))
print('Os valores sorteados foram {}'.format(numeros))
print('O maior número sorteado foi {} \nO menor número sorteado foi {}'.format(max(numeros), min(numeros)))