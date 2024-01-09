def ficha(a , b = 0):
    if a == '':
        a = 'desconhecido'
    if b == '':
        b = 0
    return (f'O jogador {a} fez {b} gols no campeonato')
nome = str(input('Qual o nome do jogador?: '))
gols = input('Quantos gols ele fez no jogo?: ')
print(ficha(nome, gols))