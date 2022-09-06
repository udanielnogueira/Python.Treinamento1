estado = {}
brasil = []

for i in range(0,2):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    
    # Appende de cópia de dicionário
    brasil.append(estado.copy())

for estado in brasil:
    print(estado['uf'], estado['sigla'])
