count = 0
while True:
    print('-=' * 20)
    n = int(input('Digite um número que você queira ver a tabuada: '))
    print('-=' * 20)
    if n >= 0:
        for count in range(1, 10):
            print('{} x {} = {}'.format(n, count, n * count))
    else:
        break
print('FIM DO PROGRAMA')
