# Operadores logicos com if


# retorna true se os 2 forem true
#comparacao1 and comparacao2

# retorna true se um dos dois forem true
#comparacao1 or comparacao2

# not equivale a !value
# se uma variavel vier vazia, é uma maneira de você autenticar
a = 0
if not a:
    print('Por favor, preencha o valor de A')

#in é para verificar se tem algo dentro tipo um [2] da variavel
nome = 'gabriel'
if 'g' in nome:
    print("Existe a letra g no meu nome")

#not in é o inverso do in, se não tiver isso, ele executa
if 'na' in nome:
    print('Não tem')