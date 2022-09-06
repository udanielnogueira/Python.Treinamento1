pessoas = list()
dados = list()

for i in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))

    pessoas.append(dados[:])

    dados.clear()

print(pessoas)
