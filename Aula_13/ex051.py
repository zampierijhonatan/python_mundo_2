primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print(i, end='-> ')
print('Acabou')