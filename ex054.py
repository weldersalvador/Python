quantidade1 = 0
quantidade2 = 0
for c in range(1 , 8):
    data = int(input(('Digite a {} data: '.format(c))))
    if data <= 2004:
        quantidade1 += 1
    else:
        quantidade2 += 1
print('Ao todo há {} pessoas maiores de idade \nE {} pessoas menores de idade'.format(quantidade1 , quantidade2))

