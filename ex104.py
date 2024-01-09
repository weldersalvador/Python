
def leiaInt(a):
    while a.isnumeric() != True:
            print('Erro! Digite um número válido!')
            a = input('Digite um número: ')
    return(f'O número digitado foi {a}')


numero = leiaInt('Digite um número: ')
print(numero)

