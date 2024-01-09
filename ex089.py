lista = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cont = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    lista.append([nome, [nota1, nota2], media])
    while not cont in 'SsNn':
        cont = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if cont in 'Nn':
        break
print(f"{" "No.: < 5}{""NOME"": < 5}{""MEDIA"" : < 5}")
for i , p in enumerate(lista):
    print(f'{i:<5}{p[0]:<5}{p[1]:<5}')
