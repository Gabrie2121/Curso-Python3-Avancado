# Calculadora Logica em While

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero.')
        break
    # podia ser continue

        

    num_1 = int(num_1)
    num_2 = int(num_2)
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Digite um operador valido (+,-,/,*)')
        
    sair = input('Deseja sair?s [s]im ou [n]ão: ')
    if sair == 's':
        break