lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Número duplicado! Não irei adicionar.')
        lista.remove(numero)
    else:
        print('Adicionado...')
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    lista.append(numero)
    if cont in 'Nn':
        break
lista.sort()
print(f'Os números digitados foram {lista}')
