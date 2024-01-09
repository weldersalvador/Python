lista = []
count = 0
while True:
    numero = int(input('Digite um número: '))
    cont = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    count += 1
    lista.append(numero)
    while not cont in 'SsNn':
        cont = str(input('Quer cotinuar?[S/N]: ')).strip().upper()[0]
    if cont in 'Nn':
        break
print('=' * 60)
lista.sort(reverse=True)
print('Você digitou {} números'.format(count))
print('A lista ordenada e de trás para frente é {}'.format(lista))
if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado e não está na lista')
print('=' * 60)
