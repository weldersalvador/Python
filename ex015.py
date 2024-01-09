d = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos km percorridos?: '))
t = (60 * d) + (0.15 * km)
print('O total a ser pago é {:.2f}R$'.format(t))