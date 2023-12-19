"""
Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:

Escolha do usuário Operação:

1 - Média entre os números digitados
2 - Maior valor dos números digitados
3 - Menor valor dos números digitados
4 - Divisão inteira dos números digitados
"""

num1=int(input("Informe o primeiro numero: "))
num2=int(input("Informe o segundo numero: "))

print("1 - Média entre os números digitados")
print("2 - Maior valor dos números digitados")
print("3 - Menor valor dos números digitados")
print("4 - Divisão inteira dos números digitados")

operacao=int(input("Informe o numero da operação:"))

match operacao:
    case 1:
        resultado=(num1+num2)/2
        print(f"A média entre os números digitados é {resultado}")
    case 2:
        resultado= max(num1, num2)
        print(f"O maior valor dos números digitados é {resultado}")
    case 3:
        resultado = min(num1, num2)
        print(f"O maior valor dos números digitados é {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 // num2
            print(f"A divisão inteira dos números digitados é {resultado}")
        else:
            print("Erro na divisão por zero")
    case _:
        print("Opção invalida!")



