lista1 = []
lista2 = []
maior = menor = 0
contador_pessoas = cont_peso1 = cont_peso2 = 0
while True:
    lista1.append((str(input('Digite o nome da pessoa: '))))
    lista1.append((float(input('Digite o peso da pessoa: '))))
    lista2.append(lista1[:])
    lista1.clear()
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if len(lista2) == 0:
        meior  = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    while not cont in 'SsNn':
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if cont in 'Nn':
        break
'''F'''


print(f'Ao todo foram cadastradas {len(lista2)} pessoas')
print(f'O maior peso é: {maior}')
print(f'O menor peso é {menor}')


