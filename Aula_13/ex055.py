#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulher_menos_20 = 0


for p in range(1,5):
    print('\n----- {}ª PESSOA -----\n'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    media_idade += idade
    
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
        
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
        
media_idade = media_idade / 4

print('\nA média de idade do grupo é de {} anos.\n'.format(media_idade))
print('\nO homem mais velho se chama {}\n'.format(homem_mais_velho))
print('\nAo todo, são {} mulheres com menos de 20 anos\n'.format(mulher_menos_20))