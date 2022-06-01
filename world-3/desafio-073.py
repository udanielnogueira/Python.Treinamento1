'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem da colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.

b) Os 4 últimos colocados.

c) Uma lista em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

times = ('Palmeiras', 'Atlético MG', 'Corinthians', 'Coritiba', 'São Paulo', 'Athletico PR', 'Botafogo', 'Flamengo', 'Santos', 'AméricaMG', 'Fluminense', 'Internacional', 'Avaí', 'Bragantino', 'Goiás', 'Cuiabá', 'Atlético GO', 'Juventude', 'Ceará', 'Fortaleza')

for i in range(0,5): # ou usar print(times [0:5])
    print(f'{i+1}º colocado: {times[i]}') 

print()

for i in range(16,20): # ou usar print(times [-4:])
    print(f'{i+1}º colocado: {times[i]}') 

print()

print('Times em ordem alfabética:', sorted(times))

print()

p = times.index('Flamengo')
print(f'Flamengo está na {p+1}º posição')
