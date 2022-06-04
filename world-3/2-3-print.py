'''
Exibindo elementos da lista
'''

lista_numeros = list(range(100,110))

# Exibindo elementos
for numero in lista_numeros:
    print(f'{numero} ', end='')

print()

# Exibindo elementos
print(*lista_numeros, sep=' ')

print()

# Exibindo endereços e elementos
for index, numero in enumerate(lista_numeros):
    print(f'{index}->{numero} ')
