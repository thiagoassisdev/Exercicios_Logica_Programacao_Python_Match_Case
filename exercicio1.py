"""•
Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha
e faça as seguintes operações:

Opcao = 1: adicione 5 ao valor de X e exiba na tela.
Opcao = 2: subtraia 4 ao valor de X e exiba na tela.
Opcao = 3: dobre o valor de X e exiba na tela.
"""
num = float(input("Digite um numero: "))

print("Opcao 1: adicione 5 ao valor de X e exiba na tela.")
print("Opcao 2: subtraia 4 ao valor de X e exiba na tela.")
print("Opcao 3: dobre o valor de X e exiba na tela.")

operacao = int(input("Digite a operação que deseja executar: "))

match operacao:
    case 1:
        num=num + 5
    case 2:
        num=num - 4
    case 3:
        num=num * 2
    case _:
        print("Opção invalida.")

print(f"O resultado da operação escolhida é: {num:.2f}")
