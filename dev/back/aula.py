print ("Bem vindo ao sistema Ian Couto!")

int(input("Digite sua idade para saber se você pode ou não votar:")) 

#Exemplos de variáveis

nome, sobrenome, idade, sexo = ( "Marcos", "Paulo", 12, "mulher")
 
#Uso das variáveis, if elif e else, print  

if idade >= 16 and idade < 18:
    print(nome, sobrenome, "pode votar se quiser pois tem:", idade, "anos de idade." )

elif idade >= 18 and idade <= 60:
    print(nome, sobrenome,  "é obrigado a votar pois tem:", idade, "anos de idade." )

elif idade > 60:
    print(nome, sobrenome, "pode votar se quiser pois tem mais de", idade, "anos de idade." )

else:
    print(nome, sobrenome, "não pode votar pois tem", idade, "anos de idade e precisa de no mínimo 16!")

salario = float (1000)
salario = str (salario)

print("A ", nome, sobrenome, "Recebeu em Fevereiro a quantia de ", salario)
print ("Depois de alguns meses recebeu tera 10% de aumento")

salario= float(salario)
salario = salario + salario * (10/100)
print("seu novo salário será de" +str(salario))