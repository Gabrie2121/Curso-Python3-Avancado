"""
Formatando valores com modificadores
:s - Texto (str)
:d - Inteiro (int)
:f - Real (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(caractere)(> ou < ou ^) (qtd)(TIPO -s,d ou f)
> - esquerda
< - direita
^ - centro
"""
# usando .format para formatar decimais do float :f
num_1 = 10
num_2 = 3
divisao = num_1/num_2
print('{:.2f}'.format(divisao))

# usando :(caractere)(> ou < ou ^) para gerenciar tamanho
num_3 = 1
print(f'{num_3:0>10}')
#:0 == quer que seja preenchido com 0
#> e os zeros estarão a esquerda
#10 que o valor independentemente tera 10 casas
num_4 = 1150
print('{:0<10}'.format(num_4))

# formatando numero inteiro como float
print(f'{num_4:.2f}')
#da para unir tudo
print(f'{num_4:0>10.2f}')

# usando .format para string :s
nome = 'Gabriel Miranda'
print('{:s}'.format(nome))
#print(f'{nome:s}')
print(f'{nome:#^17}')

# usando .format na variavel
nome_formatado = '{n:0<20}'.format(n=nome) 
print(nome_formatado)

# usando ljust 
# ljust (left just) preenche o lado esquerdo com uma quantidade de selecionado
# assim como o rjust preenche o lado direito
print(nome.ljust(20, '#'))

# usando lower, upper, title
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # Primeiras letras maiusculas