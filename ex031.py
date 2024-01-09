km = float(input('Digite a distância da sua viagem em km: '))
p1 = 0.5 * km
p2 = 0.45 * km
if km<= 200:
    print('O preço a ser pago será de {}R$'.format(p1))
else:
    print('O preço a ser pago será de {}R$'.format(p2))