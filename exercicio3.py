"""
Crie um menu com as 4 operações matemáticas (soma, subtração, multiplicação e divisão) que devem ser
executadas com 2 números reais (float) de acordo com a escolha (opção) do usuário:

Opcao = 1: soma dos 2 números.
Opcao = 2: subtração dos 2 números.
Opcao = 3: multiplicação dos 2 números.
Opcao = 4: divisão dos 2 números.
"""
num1= float(input("Informe o primeiro numero: "))
num2= float(input("Informe o segundo numero: "))

print("Opcao = 1: soma dos 2 números.")
print("Opcao = 2: subtração dos 2 números.")
print("Opcao = 3: multiplicação dos 2 números.")
print("Opcao = 4: divisão dos 2 números.")

operacao=int(input("Informe o numero da operação que deseja executar:"))

match operacao:
    case 1:
        resultado=num1+num2
    case 2:
        resultado=num1-num2
    case 3:
        resultado=num1*num2
    case 4:
        resultado=num1/num2
    case _:
        print("Operação solicitada invalida!")
print(f"O resultado da operação escolhida é {resultado:.2f}")

