lista = list()
dic = dict()
gols = list()
while True:
    dic['nome'] = str(input('Nome do jogador: '))
    dic['partidas'] = int(input(f'Quantas partidas {dic["nome"]} jogou?: '))
    for count in range(0, dic['partidas']):
        gol = int(input(f'Gols na partida {count}: '))
        gols.append(gol)
    dic['gols'] = gols[:]
    gols.clear()
    lista.append(dic.copy())
    continuar = input('Deseja continuar?[S/N]: ')
    while not continuar in 'SsNn':
        continuar = input('Deseja continuar?[S/N]: ')
    if continuar in 'Nn':
        break
print(lista)
for i, v in enumerate(lista):
    print(f'Código: {i}\n')
    for k, x in v.items():
        print(f'{k}: {x},\n', end=' ')
print()
while True:
    jogador = int(input('Qual jogador você deseja ver as estatisticas?: (999 para parar): '))
    if jogador == 999:
        break
    elif jogador > len(lista):
        print('ERRO! Digite novamente: ')
    else:
        print(f'ESTATÍSTICA DO JOGADOR {lista[jogador]["nome"]}')
        for l, m in enumerate(lista[jogador]["gols"]):
            print(f'No jogo {l} fez {m} gols')

    print('-=' * 20)
print('OBRIGADO! VOLTE SEMPRE')