a = int(input('Ano de nascimento: '))
i = 2022 - a
print('Quem nasceu em {} tem {} anos'.format(a , i))
if i < 18:
    print('Você ainda irá se alistar! Seu alistamento será em '.format(a + 18))
elif i == 18:
    print('Ja está na hora de você se alistar!')
else:
    print('Ja passou do tempo de você se alistar! Seu alistamento foi em {}'.format(2022 - (i - 18)))