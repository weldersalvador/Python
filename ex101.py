def voto(idade):
    if  idade >= 18 and idade < 75 :
        return('o voto é obrigatório!')
    elif idade < 0:
        return('Ta de pegadinha comigo?')
    elif idade >= 75:
        return('O voto é OPCIONAL!')
    else:
        return('O voto não é obrigatório!')


ano = int(input('Digite o seu ano de nascimento: '))
idade = 2022 - ano
print(f'Com {idade} anos: {voto(idade)}')