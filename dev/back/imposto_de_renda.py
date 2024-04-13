print("Bem vindo ao sistema da receita federal!")

nome = input("digite seu nome: ")
salario = int(input(print("Digite seu salário mensal: ")))

quinze = salario * 0.15
vinte_e_cinco = salario * 0.25

sobra = salario - quinze
total = salario - vinte_e_cinco

if salario <= 2499:
    print("Você está isendo de pagar impostos!")

elif salario >= 2500 and salario <= 4999:
    print (nome, "Seu salário é:", salario, "e você deverá parar o Imposto de renda de 15%, total de: ", quinze, "e vai lhe sobrar um total de:", sobra, "FAZ O L!")

else:
    print(nome, "Seu salário é:", salario, "e você deverá parar o Imposto de renda de 25%, total de: ", vinte_e_cinco,  "e vai lhe sobrar um total de:", total, "FAZ O L!")