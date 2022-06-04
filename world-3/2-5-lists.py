'''
Referenciando listas e Copiando valores de listas
'''

a = [0, 1, 2, 3]

# Ligando a com b
b = a

# Copiando a para c (fatiamento)
c = a[:]

# Alterando o valor de b, altera o valor de a
b[0] = 9

print(a)
print(b)
print(c)
