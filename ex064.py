n = s = count = 0
n = int(input('Digite um número (999 para parar o programa): '))
while n != 999:
    count += 1
    s += n
    n = int(input('Digite um número (999 para parar o programa): '))
print('A soma dos {} números digitados foi {}'.format(count , s))