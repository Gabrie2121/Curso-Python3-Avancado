# formatação de strings (fstrings)

nome = 'Gabriel'
idade = 20
altura = 1.80
e_maior = idade> 18
peso = 107
imc = peso/(altura*altura)

#necessario o f antes
# :.2f é apenas 2 casa decimais, assim como :.5f seria 5 casas
# o 2 siginifica as casas, e o f significa format apos ponto flutuante
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
# .format no final você coloca as variaveis em ordem como vc quer ela dentro da string
# para usar o :.2f no .format tem que colocar dentro das chaves {}
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
#você tambem pode enumerar e pode mexer na ordem
print('{0} {0} tem {1} anous e seu imc é {2:.2f}'.format(nome, idade, imc))
#pode tambem criar uma abreviação para a variavel e pode mexer na ordem
print('{n} {n} tem {i} anous e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
