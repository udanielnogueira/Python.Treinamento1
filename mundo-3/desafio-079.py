'''
Crie um programa onde o usuário possa digitar valores numéricos e cadastre-os em uma única lista. Caso
o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''

valores = []

while True:
    valor = int(input('Valor: '))

    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor repetido, digite outro.')
    
    resposta = str(input('Continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break
    else:
        continue

valores.sort()
print(valores)
