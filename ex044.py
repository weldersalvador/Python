c = float(input('Preço das compras: '))
print('=' * 20)
print('FORMA DE PAGAMENTO: ')
print('=' * 20)
print('DIGITE [1] PARA COMPRAR A VISTA')
print('DIGITE [2] PARA COMPRAR Á VISTA NO CARTÃO')
print('DIGITE [3] PARA COMPRAR 2X NO CARTÃO')
print('DIGITE [4] PARA COMPRAR 3X NO CARTÃO')
c2 = input('Qual é a opção?: ')
if c2 == '1':
    print('O valor a ser pago será de {}R$'.format(c - 10 * c / 100))
elif c2 == '2':
    print('O valor a ser pago será de {}R$'.format(c - 5 * c / 100))
elif c2 == '3':
    print('O valor a ser pago será de {}R$'.format(c))
elif c2 == '4':
    c3 = int(input('Quantas parcelas?: '))
    print('Sua compra será parcelada em {}x de {} com juros!'.format(c3 , c / c3 + c * 20 / (100 * c3)))
    print('O valor a ser pago terá juros e o preço total será de {}R$'.format(c + 20 * c / 100))
else:
    print('Por favor, digite o número correto')

