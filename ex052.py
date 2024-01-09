n = int(input('Digite um número inteiro: '))
quant = 0
for c in range(1 , n + 1):
    if n % c == 0:
        quant += 1
if quant == 2:
    print('O número {} foi dividido {} vezes'.format(n , quant))
    print('E por isso, ele será primo!')
else:
    print('O número {} foi dividido {} vezes \nE por isso, ele não será primo!'.format(n , quant))



