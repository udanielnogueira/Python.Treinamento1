lanches = ['doritos', 'hamburguer', 'batata-frita', 'pudim']

print(type(lanches))

def exibir():
    print(lanches)

exibir()

lanches.append('salgadinho')
lanches.insert(0, 'piraque')

exibir()

# Remove o último
lanches.pop() 
# Remove pelo índice
lanches.pop(2)
# Remove pelo elemento
lanches.remove('piraque')

exibir()

if 'refrigerante' in lanches:
    lanches.remove('refrigerante')

'''
Uma outra maneira de remover um elemento
del lanche[2]
'''
