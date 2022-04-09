frase = 'Aprendendo Python'
print('Frase original:', frase)

print('Frase com replace:', frase.replace('Python','Programação'))

# a string é imutável, print(frase) não exibiria a mudança

print('Todas as letras em maiúsculo:', frase.upper())
print('Todas as letras em minúsculo:', frase.lower())

print('A primeira letra em maiúsculo:', frase.capitalize())
print('Todas as iniciais em maiúsculo:', frase.title())

print()

print('Frase com espaços:')
frase2 = '     Look this!     '
print(frase2)
print('Removendo os espaços:\n' + frase2.strip())
print('Removendo os espaços da direita:\n' + frase2.rstrip())
print('Removendo os espaços da esquerda:\n' + frase2.lstrip())
