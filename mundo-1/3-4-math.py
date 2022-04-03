n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# :.2f (2 pontos flutuantes) 
# \n (new line)
# end=' ' ou end = ' +++ '(não quebra linha com ou sem símbolos)

print('A soma é {} \nA multiplicação é {} A divisão é {:.2f}' .format(s, m, d), end=' ') # 2 pontos flutuantes
print('A divisão inteira é {} A potência é {}' .format(di, e), end=' :) ')
