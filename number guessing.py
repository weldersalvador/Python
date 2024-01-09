
from random import randint
title = 'NUMBER GUESSING'
print('=' * len(title))
print(title)
print('=' * len(title))
count2 = 0
count = 0
while True:
    random = randint(0, 10)
    number = int(input('Enter a number: '))
    while not 0 <= number <= 10:
            print('Please, enter a number between 0 and 10.')
            number = int(input('Enter a number: '))
    while not number == random:
        print('Wrong number! try again')
        number = int(input('Enter a number: '))
        count += 1 - count2
        while not 0 <= number <= 10:
            print('Please, enter a number between 0 and 10.')
            number = int(input('Enter a number: '))
    print('CONGRATULATIONS!!')
    count2 += 1
    print(f'You have tried {count + 1} times and won {count2}')
    cont = input('Do you want to continue? [Y/N]: ').upper().strip()[0]
    while not cont in 'YyNn':
            cont = input('Please, enter a valid command [Y/N]: ').upper().strip()[0]
    while not cont in 'Nn':
        number = int(input('Enter a number: '))
        while not 0 <= number <= 10:
            print('Please, enter a number between 0 and 10.')
            number = int(input('Enter a number: '))
        random2 = randint(0 , 10)
        while not number == random2:
                print('Wrong number! try again')
                number = int(input('Enter a number: '))
                while not 0 <= number <= 10:
                    print('Please, enter a number between 0 and 10.')
                    number = int(input('Enter a number: '))
                count += 1
        print('CONGRATULATIONS!!')
        count2 += 1
        print(f'You have tried {count + 1} times and won {count2}')
        cont = input('Do you want to continue? [Y/N]').upper().strip()[0]
        while not cont in 'YyNn':
            cont = input('Please, enter a valid command [Y/N]: ').upper().strip()[0]
        if cont in 'Nn':
            break
    break
print('Thanks for playing! See you next time!')


    
    
        
