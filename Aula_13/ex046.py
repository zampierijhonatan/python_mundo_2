#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Qual tabuada deseja visualizar: '))

for tabuada in range(1, 11):
    print('{} x {} = {}'.format(num, tabuada, num*tabuada))