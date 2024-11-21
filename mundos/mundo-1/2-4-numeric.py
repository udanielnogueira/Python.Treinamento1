x = input('Digite um valor: ')

print('É numérico?', x.isnumeric()) # Diz se o valor pode ser convertido num numérico ou não
print('É alfa?', x.isalpha()) # Diz se é alfabético (a...z)

print('É alfanumérico?', x.isalnum()) # Diz se é composto por letras e/ou números (a3)
