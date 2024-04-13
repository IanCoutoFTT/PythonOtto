import statistics
numeros = [4,12,3,45,6,15,3,11,9]
for _ in range(1):
    print("Números gerados:", numeros)

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numero= sum(numeros)
rep = statistics.mode(numeros) 

print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
print("Soma dos números:", soma_numero)
print("O número que mais se reprete é:", rep)
