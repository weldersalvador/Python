from sys import exit
sexo = str(input('informe seu sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Erro! Por favor, informe seu sexo corretamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))




