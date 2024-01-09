lista = []
lista2 = []
lista3 = []
while True:
    numero = int(input('Digite um número: '))
    cont = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    lista.append(numero)
    while not cont in 'SsNn':
        cont = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if numero % 2 == 0:
        lista2.append(numero)
    if numero % 2 == 1:
        lista3.append(numero)
    if cont in 'Nn':
        break
print('=' * 40)
print(f'Os números digitados foram {lista}')
print(f'Os números pares digitados foram {lista2}')
print(f'Os números ímpares digitados foram {lista3}')
print('=' * 40)

