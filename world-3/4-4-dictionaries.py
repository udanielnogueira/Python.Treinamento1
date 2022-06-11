locadora = [
    {'titulo':'Star Wars', 'ano':1977},
    {'titulo':'Avengers', 'ano':2012}
]

# append de dicionário
locadora.append({'titulo':'Matrix', 'ano':'1999'})

print(locadora)
print(locadora[1]['titulo'])

# for da maneira 1
print('\nFOR DA MANEIRA 1')
for filme in locadora:
    print(f'O {filme["titulo"]} é do ano de {filme["ano"]}.')

# for da maneira 2
print('\nFOR DA MANEIRA 2')
for i, filme in enumerate(locadora):
    print(f'O {locadora[i]["titulo"]} é do ano de {locadora[i]["ano"]}.')

# for da maneira 3
print('\nFOR DA MANEIRA 3')
for i in range(0, len(locadora)):
    print(f'O {locadora[i]["titulo"]} é do ano de {locadora[i]["ano"]}.')
