aluno = dict()
aluno['nome'] = str(input('Aluno: '))
aluno['media'] = float(input('Média: '))
print(f'O nome do aluno é {aluno["nome"]}')
print(f'Sua média vale {aluno["media"]}')
if 5 < aluno['media'] < 7.0:
    print('Situação: RECUPERAÇÃO!')
elif  aluno['media'] < 5:
    print('SITUAÇÃO: REPROVADO!')
else:
    print('Situação: APROVADO!')
