dic = {}
lista = []
listam = []
listmaior = []
soma = 0
while True:
    dic['nome'] = input('nome: ')
    dic['sexo'] = input('Sexo[F/M]: ').strip().upper()[0]
    while not dic['sexo'] in  'FfMm':
        print('Comando inválido. Por favor, digite corretamente.')
        dic['sexo'] = input('Sexo[F/M]: ').strip().upper()[0]
    dic['idade'] = int(input('Idade: '))
    continuar = input('Quer continuar?[S/N]: ').strip().upper()[0]
    lista.append(dic.copy())
    while not continuar in 'SsNn':
        print('Comando inválido. Por favor, digite corretamente.')
        continuar = input('Quer continuar?[S/N]: ').strip().upper()[0]
    soma += dic['idade']
    if dic['sexo'] == 'F':
        listam.append(dic['nome'])
    if dic['idade'] > soma / len(lista):
        listmaior.append(dic['nome'])
    if continuar in 'Nn':
        break
print(lista)
print(f'A) Ao todo foram cadastrados {len(lista)} pessoas')
print(f'B) A média de idade foi {soma / len(lista)}')
for i , k in enumerate(listam):
    print(f', Mulher {i + 1}: {k}' , end=' ')
print('C) Lista de pessoas que estão acima da média: ')
print(listmaior)