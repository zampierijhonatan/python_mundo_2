#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pess in range(1,6):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(pess)))
    
    if pess == 1:
        maior = pess
        menor = pess
    else:
        if pess >= maior:
            maior = pess
        if pess < menor:
            menor = pess
            
print('O maior peso é o {}kg e o menor é o {}kg'.format(maior, menor))
                