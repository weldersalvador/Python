soma = count1000 = count = menor = menor_valor = 0
print('-=' * 15)
print('LOJA DO WELDINHO')
print('-=' * 15)
while True:
    produto = input('Nome do produto: ')
    valor = int(input('Valor: R$'))
    if valor > 1000:
        count1000 += 1
    count += 1
    if count == 1:
        menor_valor = valor
        menor = produto
    if menor_valor > valor:
        menor_valor = valor
        menor = produto
    soma += valor
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar in 'Nn':
        break
print('O valor total da compra foi R${}'.format(soma))
print('Nessa compra, houveram {} produtos com valores acima de R$1000'.format(count1000))
print('O produto mais barato da compra foi {} que custa R${}'.format(menor, menor_valor))


