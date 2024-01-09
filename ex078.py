valores = []
maior = menor = 0
for count in range(0 , 6):
    valores.append(int(input(f'Digite um número pra a posição {count}: ')))
    if count == 0:
        maior = menor = valores[count]
    else:
        if valores[count] > maior:
            maior = valores[count]
        if valores[count] < menor:
            menor = valores[count]
print(f'Os valores digitados foram {valores}')
print(f'O maior valor é {maior}',end=' ')
for i , v in enumerate(valores):
    if v == maior:
        print(f'na posição {i}')
print(f'O menor valor é {menor}',end=' ')
for i , v in enumerate(valores):
    if v == menor:
        print(f'na posição {i}')






