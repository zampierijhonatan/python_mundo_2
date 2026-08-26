# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import os
from random import randint

os.system('cls')
alea = randint(1, 10)
tentativas = 0


print('\n- - - - - Olá, bem vindo ao jogo do número aleatório! - - - - -\n')

n = int(input('Digite seu primeiro palpite (1 ao 10): '))
while n != alea:
    n = int(input('ERROU! tente novamente (1 ao 10): '))
    tentativas += 1
    
print('\nParábens, você acertou!\n')
print('Foram necessárias {} tentativas!\n'.format(tentativas))
