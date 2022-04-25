''' 
Tuplas são imutáveis, para informações que não sofrerão modificação.
https://blog.betrybe.com/tecnologia/tuplas-em-python/
'''

jokenpo = ('pedra', 'papel', 'tesoura')

# sem usar range
for i, jogada in enumerate(jokenpo):
    print(f'{jogada} está na posição {i}')

# usando range
for i in range(0, len(jokenpo)):
    print(f'{jokenpo[i]} está na posição {i}')
