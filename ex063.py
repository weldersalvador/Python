n = int(input('Quantos termos você quer?: '))
a1 = 0
a2 = 1
count = 3
s = a1 + a2
print(a1, a2)
while count <= n:
    s = a1 + a2
    print('{}'.format(s), end='')
    a1 = a2
    a2 = s
    count += 1
    count = n + 1

print('FIM')

