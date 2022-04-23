'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
'''

maiores = 0
homens = 0
mulheresNovas = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    if idade > 18:
        maiores += 1

    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheresNovas += 1
    
    continuar = str(input(('Continuar? [S/N]: '))).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opção inválida')

print(f'Maiores de 18: {maiores}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres menos de 20: {mulheresNovas}')
