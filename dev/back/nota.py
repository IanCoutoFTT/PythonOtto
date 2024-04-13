nome = input("Digite seu nome: ")
valor1 = float(input("Digite sua 1º nota: "))
valor2 = float(input("Digite sua 2º nota: "))
valor3 = float(input("Digite sua 3º nota: "))
valor4 = float(input("Digite sua 4º nota: "))

média = ( valor1 + valor2 + valor3 + valor4)
total = (média / 4)

if total <= 59:
    print(nome, "não foi aprovada pois tem:", total, "não atingindo o mínimo de 60.0." )

else:
    print(nome, "Foi aprovado(a) com um total de:", total )