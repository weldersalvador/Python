matriz = list()
matriz1 = list()
soma = soma1 = 0
for count in range(0 , 9):
    numero = int(input('Digite o valor para a matriz: '))
    matriz1.append(numero)
    matriz.append(matriz1[:])
    matriz1.clear()
    soma += numero
print('=' * 20)
print(matriz[0] , matriz[1] , matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('=' * 20)
print(f'A soma de todos os valores digitados vale {soma}')
print(f'A soma da terceira linha vale: {matriz[6][0] + matriz[7][0] + matriz[8][0]}')
maior_numero2 = [matriz[3][0] , matriz[4][0], matriz[5][0]]
print(f'O maior valor da segunda linha é: {max(maior_numero2)}')

