num = []
for count in range(1 , 8):
    numero = int(input(f'Digite o {count} número: '))
    num.append(numero)
    if numero in num == True:
        num.remove(numero)
for p in num:
    if p % 2 == 0:
        print(p)
print(f'Números ímpares: ')
for c in num:
    if c % 2 == 1:
        print(c)


