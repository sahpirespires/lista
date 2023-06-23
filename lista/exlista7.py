numero = []
while True:
    escolha = int(input("Adicione um número: "))
    if escolha in numero:
        numero.pop()
    numero.append(escolha)
    sair = str(input("Quer sair?"))
    if sair == "s":
        break
print(numero)