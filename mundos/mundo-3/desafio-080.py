'''
Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção. No final, mostre a lista ordenada na tela sem usar o sort().
'''

valores = []

for i in range(0,5):
    valor = int(input('Valor: '))
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        posicao = 0

        # Varrendo a lista
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                break
            posicao += 1
            
print(valores)
