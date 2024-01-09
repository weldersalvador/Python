s = float(input('Digite seu salário: '))
s1 = s + s*10/100
s2 = s + s*15/100
if s>=1250.00:
    print('Você terá um aumento para {}R$'.format(s1))
else:
    print('Você terá um aumento para {}R$'.format(s2))
