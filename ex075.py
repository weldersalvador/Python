numero = (int(input('Digite um valor: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite um ultimo valor: ')))

print('Você digitou os valores {}'.format(numero))
print('O valor 9 aparece {} vezes'.format(numero.count(9)))
m = 3 in numero
if m == False:

    print('Não possui o número 3 nos valores digitados')
else:
    print('O número 3 está na posição {}'.format(numero.index(3) + 1))
print('Os valores pares digitados foram:', end=' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
