# Condições IF, ELIF, ELSE

#como não usa chaves, ele se considera pela qtd de espaços

#se for verdadeiro entra na condição if
if True:
    print("verdadeiro.")
else:
    print('não é verdadeiro')
    
#se for falso, entra na condição else
if False:
    print("verdadeiro.")
else:
    print('não é verdadeiro')

if False:
    print('verdadeiro')
elif True:
    print('Agora é verdadeiro')
else:
    print('não é verdadeiro')