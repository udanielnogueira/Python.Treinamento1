pessoas = [['Daniel', 26], ['Ane', 25], ['Tristan', 1]]

print(type(pessoas))

print(pessoas)

print(pessoas[1][0])

for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos.', end=' ')
