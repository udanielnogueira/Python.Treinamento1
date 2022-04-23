frase = 'Mire na lua e acerte as estrelas'

# separa cada palavra
partes = frase.split()
print(partes)

# terceira palavra do split
print(frase.split()[2])

# máximo de vezes que vai separar
print(frase.split(maxsplit = 3))

print('-'.join(partes))
