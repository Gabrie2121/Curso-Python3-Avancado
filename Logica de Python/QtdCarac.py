# len - checagem quantidade de caracteres
# tipo o length do javascript

usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres,type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Precisa digitar no minimo 6 caracteres')
else:
    print('Você foi cadastrado')

string1 = input('Digite uma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracter digitados foi {len(string1)+len(string2)}')

