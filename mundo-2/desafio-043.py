'''
Desenvolva uma lógica que leia o peso e a altura de 
uma pessoa, calcule seu IMC e mostre seu status, de 
acordo com a tabala abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entra 18.5 a 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima da 40: Obesidade mórbida
'''

p = float(input('Peso: '))
h = float(input('Altura: '))

imc = p/pow(h,2)

if imc < 18.5:
    print(f'IMC: {imc} Abaixo do peso')
elif 18.5 <= imc < 25: 
    print(f'IMC: {imc} Peso ideal')
elif 25 <= imc < 30:
    print(f'IMC: {imc} Sobrepeso')
elif 30 <= imc < 40:
    print(f'IMC: {imc} Obesidade')
else:
    print(f'IMC: {imc} Obesidade mórbida')
