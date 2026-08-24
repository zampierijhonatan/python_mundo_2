nota1 = float(input('Digite o primeiro numero: '))
nota2 = float(input('Digite o segundo numero: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Nota {}, reprovado'.format(media))
elif media > 4.9 and media < 6.9:
    print('Nota {}, Recuperação'.format(media))
else:
    print('Nota {}, aprovado'.format(media))

