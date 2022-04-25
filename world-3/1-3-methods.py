''' 
Tuplas são imutáveis, para informações que não sofrerão modificação.
https://blog.betrybe.com/tecnologia/tuplas-em-python/
'''

a = (7, 8, 9)
b = (1, 2, 3, 7)
c = a + b

print('Tupla original: ', c)

# exibir em ordem alfanumérica
print('Tupla organizada: ', sorted(c))

# contar ocorrências de um elemento
print(c.count(9))

# posição de um elemento
print(c.index(9))

# posição de 7 a partir do endereço 2
print(c.index(7, 2))
