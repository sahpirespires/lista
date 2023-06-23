numeros = []
numero = int(input("Digite um número ou 0 para encerrar: "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("Digite um número ou 0 para encerrar: "))

soma = sum(numeros)
multiplicacao = 1
maior = max(numeros)
menor = min(numeros)

for num in numeros:
    multiplicacao *= num

print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
print("Maior número:", maior)
print("Menor número:", menor)