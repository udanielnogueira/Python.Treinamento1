'''
Inserindo e removendo elementos da lista
append(elemento) insert(index, elemento) pop(index) remove(elemento)
'''

lanches = ['doritos', 'hamburguer', 'batata-frita', 'pudim']

# Verificando o tipo Lista
print(type(lanches))

def exibir():
    print(lanches)

exibir()

# Inserindo elemento na lista
lanches.append('salgadinho')
lanches.insert(0, 'piraque')

exibir()

# Removendo último elemento
lanches.pop() 
# Removendo elemento pelo índice
lanches.pop(2)
# Removendo elemento pelo elemento
lanches.remove('piraque')

exibir()

if 'refrigerante' in lanches:
    lanches.remove('refrigerante')

'''
Uma outra maneira de remover um elemento
del lanche[2]
'''
