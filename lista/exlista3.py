num1=[]
while True:
    num1 .append(int(input('digite um numero:')))
    res=str(input('deseja continuar[s/n]'))
    if res in 'nn':
        break


    soma = sum(num1)
    menor = min(num1)

    print(f'Os números são {num1}')
    print(f'o menor é: {menor}')
    print(f'a soma é: {soma}')