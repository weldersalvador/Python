from sys import exit
num = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        print('Você digitou o número {}'.format(num[numero]))
        escolha = input('Quer continuar?[S/N]: ').strip().upper()
        if escolha in 'Nn':
            print('FIM')
            exit()
    else:
        while not 0 <= numero <= 20:
            numero = int(input('Digite um número de 0 a 20: '))
            if 0 <= numero <= 20:
                print('Você digitou o número {}'.format(num[numero]))
                escolha = input('Quer continuar?[S/N]: ').strip().upper()
                if escolha in 'Nn':
                    print('FIM')
                    exit()


