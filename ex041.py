idade = int(input('Qual a sua idade? '))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR')
elif 19 < idade <= 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')

