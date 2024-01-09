count18 = count_homem = count_mulher20 = 0
while True:
    print('-=' * 15)
    print('CADASTRO DE UMA PESSOA')
    print('-=' * 15)
    idade = int(input('Idade: '))
    if idade > 18:
        count18 += 1
    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo in 'Mm':
        count_homem += 1
    if sexo in 'Ff' and idade < 20:
        count_mulher20 += 1
    continuar = ' '
    while not continuar in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(count18))
print('Ao todo temos {} homens cadastrados'.format(count_homem))
print('Temos {} mulheres com menos de 20 anos'.format(count_mulher20))
