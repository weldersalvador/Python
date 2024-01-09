km = float(input('Qual é a velocidade do carro em km/h?: '))
m = (km - 80) * 7
if km<= 80:
    print('Continue...')
else:
    print('Você passou do limite de velocidade, sua multa será de {}R$'.format(m))