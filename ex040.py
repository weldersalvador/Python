n1 = float(input('Digite sua primeria nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Com essas notas sua média é {}'.format(m))
if m < 5:
    print('VOCÊ ESTÁ REPROVADO!!')
elif 5 < m < 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO!')
else:
    print('VOCÊ PASSOU!! PARABÉNS')
