def ajuda(mensagem):
    return(help(mensagem))




comando = ''
while True:
    comando = input('Digite o comando: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)