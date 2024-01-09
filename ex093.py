dic = dict()
gols = list()
dic['nome'] = str(input('Nome do jogador: '))
dic['partidas'] = int(input(f'Quantas partidas {dic["nome"]} jogou?: '))
for count in range(0 , dic['partidas']):
    gol = int(input(f'Gols na partida {count}: '))
    gols.append(gol)
dic['gols'] = gols[:]
print(f'O nome do jogador(a) é {dic["nome"]}')
print(f'Gols: {gols}')
print(f'Total de gols: {sum(gols)}')
print('-=' * 20)
for k , i in enumerate(gols):
    print(f'Na partida {k} {dic["nome"]} fez {i} gols')
print(f'Totalizando {sum(gols)} gols')
