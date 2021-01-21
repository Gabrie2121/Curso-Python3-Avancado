nome = 'Gabriel Miranda'
idade = 20
altura = 1.82
peso = 107.5
anoAtual = 2021
anoNascimento = anoAtual-idade-1
imc = peso/(altura*altura)

print('{} tem {} anos, {} de altura e pesa {}kg'.format(nome,idade,altura,peso))
print('o IMC de {n} é {i}'.format(n=nome,i=imc))
print(f'{nome} nasceu em {anoNascimento}')