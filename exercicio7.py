'''Considerando a idade de uma pessoa, exiba se ela pode doar sangue (idade entre
18 e 67 anos) ou não (idade menor que 18 anos ou maior que 67 anos).'''

#exibir a idade da pessoa

idade= int(input("Informe a idade da pessoa:"))

if (idade>=18) and (idade<=67):
    print("Você pode doar sangue!")

else:
    print ("Você não pode doar sangue!")