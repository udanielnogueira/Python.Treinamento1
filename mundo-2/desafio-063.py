'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

 0 → 1 → 1 → 2 → 3 → 5 → 8
'''

n = int(input('n: '))
fib1 = 0
fib2 = 1

i = 0
while i < n:
    print(fib1)
    fib1 = fib1 + fib2
    i = i + 1

    # só calcula mais um termo se dentro do limite
    if i < n:
        print(fib2)
        fib2 = fib1 + fib2
        i = i + 1

'''
print(fib1, fib2)

while i < n:
    fib3 = fib1 + fib2
    print(fib3)

    fib1 = fib2
    fib2 = fib3
'''
