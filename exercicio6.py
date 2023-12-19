"""
Um funcionário irá receber um aumento de acordo com o seu plano de trabalho, de acordo com a tabela abaixo:

Plano de trabalho      Porcentagem de aumento
        A                      10%
        B                      15%
        C                      20%

Faça um programa que leia o plano de trabalho e o salário atual de um funcionário e calcula e imprime o seu novo salário.
"""
salario_atual= float(input("Informe o salario atual: "))

print("1- Plano de trabalho A aumento de 10 %")
print("2- Plano de trabalho B aumento de 15 %")
print("3- Plano de trabalho C aumento de 20 %")

plano_trabalho= float(input("Informe o numero do plano de trabalho: "))

match plano_trabalho:
    case 1:
        resultado = (salario_atual*0.10)+salario_atual
    case 2:
        resultado = (salario_atual*0.15)+salario_atual
    case 3:
        resultado = (salario_atual*0.20)+salario_atual
    case 4:
        print("Opção invalida!")

print(f"O novo salario do funcionário será de R$: {resultado:.2f}")