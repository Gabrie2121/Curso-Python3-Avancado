
# acessar indices positivos [i]
texto = 'Python s2'
print(texto[2])
# acessar indices negativos
print(texto[-1])

# puxa do indice até o outro (o ultimo indice não é incluido)
# nova_string = texto[2:6]
# vai do 0 até o 6, assi como 2: vai do 2 até o final
nova_string = texto[:6]
print(nova_string)
# vai pular de 2 em 2 e pode pular quantos quiser
print(texto[0:6:2])