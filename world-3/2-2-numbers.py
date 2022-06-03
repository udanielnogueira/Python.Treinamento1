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

# Função reverse()
numeros_tres.reverse()
exibir(numeros_tres)

# Função len()
print(f'Tenho {len(numeros_tres)} elementos na lista 3')

'''
numeros_tres.reverse() ou numeros_tres.sort(reverse = True)
'''
