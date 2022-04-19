'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

totalAnos = 0
anosVelho = 0
nomeVelho = 'x'
mulheresNovas = 0

for pessoa in range(1, 5):
    nome = str(input('Nome: '))
    anos = int(input('Anos: '))
    sexo = str(input('Sexo: ')).upper()
    print( )

    totalAnos += anos

    if sexo == 'M':
        if anos > anosVelho:
            anosVelho = anos
            nomeVelho = nome
    
    if sexo == 'F':
        if anos < 20:
            mulheresNovas += 1

print(f'Média de idade: {totalAnos/4}')
print(f'Nome do homem mais velho: {nomeVelho}')
print(f'Mulheres com menos de 20 anos: {mulheresNovas}')
