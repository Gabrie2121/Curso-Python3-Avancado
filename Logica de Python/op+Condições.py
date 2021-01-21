# Condições com operadores relacionais
# == > < !

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua Idade? '))

# Limite para pegar emprestimo
idade_limite = 18

if idade >= idade_limite:
    print('{} pode pegar o emprestimo'.format(nome))
else:
    print('{} NÃO pode pegar o emprestimo.'.format(nome))


if idade >=20 and idade <=30:
    print('{} pode pegar o emprestimo'.format(nome))
else:
    print('{} NÃO pode pegar o emprestimo.'.format(nome))