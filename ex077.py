tuple = 'Welder', 'Cachorro', 'Bola', 'Sapato','Maconha', 'Duelo', 'Penteado'
for count in tuple:
    print(count, end='')
    for letras in count:
        if letras.lower() in 'aeiou':
            print(letras)