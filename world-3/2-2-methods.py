'''
Função de inserção
list()

Funções de ordenação e tamanho
sort() len()
'''

def exibir(lista):
    print(lista)

# Função list
numeros_um = list(range(0,10))
numeros_dois = list(range(0,10,2))
exibir(numeros_um)
exibir(numeros_dois)

numeros_tres = [7, 4, 3, 1, 9, 5]

# Função sort()
numeros_tres.sort()
exibir(numeros_tres)

# Função sort() com reverse
numeros_tres.sort(reverse=True)
exibir(numeros_tres)

# Função len()
print(f'Tenho {len(numeros_tres)} elementos na lista 3')
