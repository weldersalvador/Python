print('-' * 25)
print('LISTAGEM DE PREÇOS')
print('-' * 25)
tuple = ('Pão', 2.00, 'Salame', 3.00, 'Batata', 5.00, 'Feijão', 5.00 ,'Feijoada', 10.00, 'Pé de moleque', 3.00)
for count in range(0 , len(tuple)):
    if count % 2 == 0:
        print('{:.<30}'.format(tuple[count]), end='')
    else:
        print('{:>7.2f}'.format(tuple[count]))

