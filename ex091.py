from time import sleep
from random import randint
from operator import itemgetter
dic = {'jogador1': randint(1 , 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1 , 6),
       'jogador4': randint(1 , 6)}
for x , y in dic.items():
    print(f'{x} = {y}')
    sleep(0.7)
ranking = sorted(dic.items() , key=itemgetter(1) , reverse=True)
print('=' * 20)
for k , y in enumerate(ranking):
    print(f'{k + 1} lugar: {y[0]} com {y[1]}')

