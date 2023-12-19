"""
O cardápio de uma casa de lanches é dado pela tabela abaixo:

100 - Cachorro quente - R$1,70
101 - Bauro Simples - R$2,30
102 - Bauro com ovo - R$2,60
103 - Hamburguer - R$2,40
104 - Cheeseburguer - R$2,50
105 - Refrigerante - R$1,00

Escreva um algoritmo que leia o código do item adquirido pelo consumidor e a quantidade, calculando e
mostrando o valor a pagar. Não será necessário exibir o produto e o valor,vsomente o valor final."""

codigo=int(input("Informe o codigo do produto adquirido: "))
quant=int(input("Informe a quantidade: "))

match codigo:
    case 100:
        produto=1.70*quant
    case 101:
        produto=2.30*quant
    case 102:
        produto=2.60*quant
    case 103:
        produto=2.40*quant
    case 104:
        produto=2.50*quant
    case 105:
        produto=1*quant
    case _:
        print("Codigo produto invalido!")
print(f"O valor total a ser pago é de R$: {produto:.2f}")

