# Saudação baseada no horario

horario = input('Por gentileza digite qual a hora atual\n')

try:
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print('Bom dia')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde')
    elif horario >= 18 and horario <= 23:
        print('Boa noite')
    else:
        print('Digite um numero entre 0 e 23')
except:
    print('Digite um horario valido (**)')
