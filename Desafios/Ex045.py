from random import randint
from time import sleep

print('-=-'*20)
print('JO...KEN...PO!')
print('-=-'*20)
computador = randint(1,3)
print('Já sei qual vou jogar só falta vc.')
print('1 - pedra')
print('2 - papel')
print('3 - tesoura')
jogador = int(input('Pense na sua jogada e digite ele aqui: '))
print('JO...')
sleep(1)
print('Ken...')
sleep(1)
print('PO!!!')

if jogador == 1:
    print('Jogador: Pedra')
elif jogador == 2:
    print('Jogador: Papel')
else:
    print('Jogador: Tesoura')

if computador == 1:
    print('Computador: Pedra')
elif computador == 2:
    print('Computador: Papel')
else:
    print('Computador: Tesoura')

if jogador == computador:
    print('Empatamos! Isso é bom ou ruim?')
elif jogador == 1 and computador == 2:#Pedra vs Papel
    print('Ganhei! Papel cobre a pedra.')
elif jogador == 1 and computador == 3:#Pedra vs tesoura
    print('Você ganhou! Pedra bate na tesoura.')
elif jogador == 2 and computador == 1:#Papel vs pedra
    print('Você ganhou! Papel cobre pedra.')
elif jogador == 2 and computador == 3:#Papel vs tesoura
    print('Ganhei! Tesoura corta o papel.')
elif jogador == 3 and computador == 1:#Tesoura vs pedra
    print('Ganhei! Pedra bate na tesoura.')
else:#Tesoura vs papel
    print('Você ganhou! Tesoura corta o papel.')