'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

matriz = [[], [], []]

pares = []
soma_terceira_coluna = 0
maior_segunda_linha = 0

for linha in range(0,3):
    for coluna in range(0,3):
        n = int(input('n: '))
        matriz[linha].append(n)

        if n % 2 == 0:
            pares.append(n)
        
        if coluna == 2:
            soma_terceira_coluna += n
        
        if linha == 1:
            if n > maior_segunda_linha:
                maior_segunda_linha = n


for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()

print(f'Pares: {pares}')
print(f'Soma da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_segunda_linha}')
