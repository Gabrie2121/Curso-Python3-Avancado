# algumas funções que podem ser uteis
# iddigit, isdecimal, isnumerical
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

#isdigit e positivo
if num1.isdigit() == True and num2.isdigit() == True:
    print(int(num1)+int(num2))
else:
    print('Digite apenas numeros inteiros sem . ou ,')


# try

try:
    print(int(num1)+int(num2))
except:
    print('error')