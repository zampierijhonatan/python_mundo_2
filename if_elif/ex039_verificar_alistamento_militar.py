idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Voce ainda tem alguns anos até se alistar!')
elif idade > 15 and idade < 18:
    print('Voce está quase com idade para se alistar!')
else:
    print('Já passou a hora de se alistar!!')