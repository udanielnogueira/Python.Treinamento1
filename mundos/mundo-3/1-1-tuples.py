''' 
Tuplas são imutáveis, para informações que não sofrerão modificação.
https://blog.betrybe.com/tecnologia/tuplas-em-python/
'''

jokenpo = ('pedra', 'papel', 'tesoura')

print(jokenpo)

print(jokenpo[0].capitalize())

for jogada in jokenpo:
    print(f'Vou escolher {jogada}')

for i in range(0, len(jokenpo)):
    print(jokenpo[i])
