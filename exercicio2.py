"""
Pela tabela a seguir, mostre a descrição e o preço do produto após a digitação do código pelo
usuário. Se o produto não estiver cadastrado, emitir mensa¬gem avisando. OBS: utilizar o Desvio Condicional
de Múltipla Escolha.

Código 	Descrição 	Preço R$ 
01 	    Caneta   	1.20
02 	    Lápis    	0.80
03 	    Caderno 	4.50
04 	    Borracha 	1.00
05 	    Régua    	1.50
"""
cod = int(input("Informe o codigo do produto: "))

match cod:
    case 1:
        print("Caneta valor R$1.20")
    case 2:
        print("Lapis valor R$0.80")
    case 3:
        print("Caderno valor R$4.50")
    case 4:
        print("Borracha valor R$1.00")
    case 5:
        print("Régua valor R$1.50")
    case _:
        print("Codigo produto não cadastrado! ")