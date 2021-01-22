# Contagem de letras

nome = input('Digite seu nome\n')

try:
    if len(nome) <= 4:
        print(f'O nome {nome} é muito pequeno')
    elif len(nome) <= 6:
        print(f'O nome {nome} é normal')
    else:
        print(f'O nome {nome} é muito grande')
except:
    print('Digite um nome valido')
