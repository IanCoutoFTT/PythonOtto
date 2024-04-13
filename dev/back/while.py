nome = input("Digite seu nome: ")
soma = 0 
contador = 0
media = 0 

while True:
    nota = float(input("Digite sua nota:"))
    contador = contador + 1
    media = soma / contador

    if nota == 0.0:
        print(nome, "A soma de suas notas é:", soma)
        print ("O númedo de notas somas foram de: ", contador)
        print ("sua média final é de: ", media)
        break
    soma = soma + nota
    