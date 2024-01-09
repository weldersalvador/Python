from time import sleep
def contador():
    print('-' * 36)
    print('Irei contar de 0 até 10 de um em um: ')
    print('-' * 36)
    for count in range(0 , 11):
        print(count, end=' ', flush=True)
        sleep(0.5)
    print('-' * 46)
    print('Agora irei contar de 0 até 10 de dois em dois: ')
    print('-' * 46)
    for count2 in range(0, 12 , 2):
        print(count2 , end=' ', flush=True)
        sleep(0.5)
    print('-' * 17)
    print('Agora é a sua vez!')
    print('-' * 17)
    numero1 = int(input('início: '))
    numero2 = int(input('Final: '))
    passo = int(input('Passo: '))
    if numero2 < numero1:
        if passo < 0:
            for count3 in range(numero1 , numero2 + passo, passo):
                print(count3)
                sleep(0.5)
        if passo > 0:
            passo = passo * (-1)
            for count3 in range(numero1 , numero2 + passo, passo):
                print(count3)
                sleep(0.5)
        if passo == 0:
            passo = -1
            for count3 in range(numero1 , numero2 + passo, passo):
                print(count3)
                sleep(0.5)
    if numero2 > numero1:
        if passo < 0:
            print('ERRO! Por favor, digite novamente:')
            passo = int(input('Passo: '))
        if passo > 0:
            for count3 in range(numero1 , numero2 + passo, passo):
                print(count3)
                sleep(0.5)
        if passo == 0:
            passo = 1
            for count3 in range(numero1 , numero2 +passo , passo):
                print(count3)
                sleep(0.5)

    
contador()
