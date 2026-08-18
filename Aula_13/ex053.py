#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
menor = 0
maior = 0


for nass in range(1, 8):
    idade = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(nass)))
    ano = atual - idade
    
    if ano <=17:
        menor += 1
    else:  
        maior += 1
        
print('O total de menores é: {}'.format(menor))
print('O total de maiores é: {}'.format(maior))


