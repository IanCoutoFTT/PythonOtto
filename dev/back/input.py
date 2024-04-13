nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <= 17:
    print (nome, "tem", idade, "anos de idade então tá safe.")

else: 
    print(nome, "tem", idade, "anos de idade e já pode ser preso.")