#Escolha para velocidade ou distância de um mruv
escolha = str(input('Distancia ou velocidade? [D/V]: ')).upper().strip()[0]
#Caso o usuário não faça a entrada correta
while not escolha in 'DdVv':
    print('Por favor, digite um comando válido. ')
    escolha = str(input('Distancia ou velocidade? [D/V]: ')).upper().strip()[0]
#Calculo da distância com os dados
if escolha in 'Dd':
    existe = str(input('Tem velocidade inicial?[S/N]: ')).upper().strip()[0]
    while not existe in 'SsNn':
        print('Por favor, digite um comando válido')
        existe = str(input('Tem velocidade inicial?[S/N]: ')).upper().strip()[0]
    if existe in 'Ss':
        vel = float(input('Velocidade inicial(m/s): '))
        pos = float(input('Posição inicial(m): '))
        aceleração = float(input('Aceleração(m/s2): '))
        tempo = float(input('Tempo percorrido: '))
        posi = pos + (vel * tempo) + ((aceleração * (tempo**2)) / 2)
    else:
        pos = float(input('Posição inicial(m): '))
        vel = 0
        aceleração = float(input('Aceleração(m/s2): '))
        tempo = float(input('Tempo percorrido(s): '))
        posi = pos + (vel * tempo) + ((aceleração * (tempo**2)) / 2)
    print(f'A distância percorrida pelo móvel em {tempo} segundos é de {posi}m')
    print(f'A equação da distância percorrida pelo objeto em função do tempo é: y(t) = {pos} + {vel}t + {aceleração}t²/2')
    #Concavidade da parabola criada
    if aceleração < 0:
        print('A equação da posição do movimento em função do tempo é um parabábola com convidade apontada para baixo.')
    elif aceleração == 0:
        print('A equação da posição do moviemnto em função do tempo é uma reta crescente. (MU)')
    else:
        print('A equação da posição do movimento em função do tempo é uma parábola com convidade apontada para cima. ')
#Calculo da velocidade com os dados
if escolha in 'Vv':
    existe = str(input('Tem velocidade inicial?[S/N]: ')).upper().strip()[0]
    while not existe in 'SsNn':
        print(input('Por favor, digite um comando válido'))
        existe = str(input('Tem velocidade inicial?[S/N]: ')).upper().strip()[0]
    if existe in 'Ss':
        vel1 = float(input('Velocidade inicial(m/s): '))
        aceleração1 = float(input('Aceleração(m/s2): '))
        tempo1 = float(input('Tempo percorrido: '))
        velocidade1 = vel1 + aceleração1 * tempo1
    else:
        vel1 = 0
        aceleração1 = float(input('Aceleração(m/s2): '))
        tempo1 = float(input('Tempo percorrido: '))
        velocidade1 = aceleração1 * tempo1
    print(f'A velocidade após {tempo1} segundos percorridos é de {velocidade1}m/s')
    print(f'A equação da velociade em função do tempo é: V(t) = {vel1} + {aceleração1}t')
    #Característica da reta da velocidade
    if aceleração1 < 0:
        print('A equação da velocidade em função do tempo será uma reta decrescente com coeficiente linear (aceleração) negativa.')
    elif aceleração1 == 0:
        print('A equação da velocidade em função do temp será uma reta constante. (MU)')
    else:
        print('A equação da velocidade em função do tempo será uma reta crescente com coeficiente linear (aceleração) positiva')