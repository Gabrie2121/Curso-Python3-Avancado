# Faça o programa informar se o numero inteiro é par ou impar

numero = input('Digite um numero inteiro\n')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} é impar')
except:
    print(f'Por favor digite um numero inteiro valido')
