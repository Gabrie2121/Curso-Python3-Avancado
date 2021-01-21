#entrada de dados do usuario com input

#O que o usuario digitar na tela vai ser atribuida pra variavel em questão

nome = input("Qual o seu nome? ")
print(f'O usuario digitou {nome} e o tipo da variavel é {type(nome)}')

nome1 = input("Qual o seu nome? ")
idade= input("Qual a sua idade? ")

#int(idade) é um parse para outro tipo
ano_nascimento = 2021-int(idade)
print('\n{} tem {} anos de idade'.format(nome1, idade))
print('nasceu em {}'.format(ano_nascimento))

#calculadora que só faz soma
#parse pode ser chamado tambem antes do pedido de input
numero1 = int(input('Digite um numero '))
numero2 = int(input('Digite outro numero '))
resultado = numero1+numero2
print(resultado)