a1 = float(input('Digite o valor do primeiro termo: '))
r = float(input('Digite o valor da razão: '))
print('Os 10 primeiros termos dessa PA é:')
c = 0
while c < 10:
    c = c + 1
    print(a1 if c == 1 else a1 + (c - 1) * r, end=' ')