from sys import exit
dic = dict()
dic['nome'] = input('Nome: ')
dic['nascimento'] = int(input('Ano de nascimento: '))
dic['ctps'] = int(input('Carteira de trabalho: (0 não tem): '))
if dic['ctps'] == 0:
    print(f'Nome tem valor {dic["nome"]:>3}')
    print(f'Idade tem valor {2022 - dic["nascimento"]:>3}')
    print(f'ctps tem valor {0:>3}')
    exit()
else:
    dic['ano'] = int(input('Ano de contratação: '))
    dic['sal'] = float(input('Salário: '))
    print(f'Nome tem valor {dic["nome"]}')
    print(f'Idade tem valor {2022 - dic["nascimento"]}')
    print(f'ctps tem valor {dic["ctps"]}')
    print(f'Contratação tem valor {dic["ano"]}')
    print(f'Salário tem valor {dic["sal"]}')
    print(f'Aposentadoria tem valor {35 + (2022 - dic["ano"])}')

