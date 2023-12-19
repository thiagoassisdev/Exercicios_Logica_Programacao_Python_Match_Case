'''Analise combinatoria maior de três numeros'''

num1 = int(input("informe o primeiro numero:"))
num2 = int(input("Informe o segundo numero:"))
num3 = int(input("Informe o terceiro numero:"))


if (num1>num2) and (num2>num3):
    print(num1)

if (num1>num3) and (num3>num2):
    print(num2)

if (num2>num1) and (num1>num3):
    print(num2)

if (num2>num3) and (num3>num1):
    print(num2)

if (num3>num1) and (num1>num2):
    print(num3)

else: (num3>num2) and (num2>num1)
print(num3)
