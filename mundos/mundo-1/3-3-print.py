nome = input('Digite seu nome: ')

print('Olha isso {:20}!' .format(nome)) # 20 espaços
print('Olha isso {:>20}!' .format(nome)) # alinhado à direita
print('Olha isso {:<20}!' .format(nome)) # alinhado à esquerda
print('Olha isso {:^20}!' .format(nome)) # centralizado
print('Olha isso {:=^20}!' .format(nome)) # centralizado entre sinais
