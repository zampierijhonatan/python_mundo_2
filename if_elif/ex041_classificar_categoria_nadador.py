idade = int(input('Olá atleta! Digite sua idade: '))

if idade < 10:
    print('Categotia MIRIM')
elif idade < 15:
    print('Categoria INFANTIL')
elif idade < 20:
    print('Categoria JÚNIOR')
elif idade < 26:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')