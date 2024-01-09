import random
gerador = 'GERADOR DE SENHAS'
print('=' * len(gerador))
print(gerador)
print('=' * len(gerador))
n = int(input('Quantas senhas você quer?: '))
k = int(input('Quantos caracteres?: '))

def senhas(numero):
    lista = 'A', 'a' , 'B' , 'b' , 'C' , 'c' , 'D' , 'd' , 'E' , 'e' , 'F' , 'f' , 'G' , 'g' , 'H' , 'h' , 'I' , 'i' , 'J' , 'j' , 'K', 'k' , 'L' , 'l' , 'M' , 'm' , 'N' , 'n' , 'O' , 'o' , 'P' , 'p', 'Q' , 'q' , 'R' , 'r' , 'S' , 's' , 'T' , 't' , 'U' , 'u' , 'V' , 'v' ,'W' , 'w' , 'X' , 'x' , 'Y' , 'y' , 'Z' , 'z' , '@' , '#' , '$' , '%' , '&' , '*' , '(' , ')'
    rand = random.choices(lista , k = k)
    for count in range(1 , numero + 1):
        x = print(f' senha {count}: ' , ''.join(random.choices(lista , k = k)))
        
print('-' * 30)
senhas(n)
print('-' * 30)