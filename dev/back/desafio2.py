#Colocando variáveis
nome = ("Mariana")
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um segundo valor: "))
valor3 = int(input("Digite um terceiro valor: "))
valor4 = int(input("Digite um quarto valor: "))

média = ( valor1 + valor2 + valor3 + valor4)
total = (média / 4)

print ("As notas de", nome, "são:", valor1, ",", valor2, ",", valor3, ",", valor4, "e sua média final é", total)

if total >= 60 and total < 70:
    print(nome, "não foi aprovada pois tem:", total, "não atingindo o mínimo de 70.0." )

elif total >= 70 and total <= 100:
    print(nome, "Foi aprovada" )


    print(type(valor1))
    print(type(total))