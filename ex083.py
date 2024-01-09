numero = input('Digite a sua expressão: ')
if (numero.count('(') + numero.count(')')) % 2 == 0:
    print('A expressão está correta! ')
else:
    print('A expressão é inválida!')