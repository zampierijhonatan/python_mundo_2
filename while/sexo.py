#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]

while sexo != "F" and sexo != "M":
    
    sexo = str(input('Digite seu sexo valido! (M/F): ')).strip().upper()[0]
    
if sexo == "F":
    print('Olá, mulher!')
else:
    print('Olá, homem!')