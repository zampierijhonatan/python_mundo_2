lado1 = float(input('Digite o tamanho do primeiro lado: '))
lado2 = float(input('Digite o tamanho do segundo lado: '))
lado3= float(input('Digite o tamanho do terceiro lado: '))

if lado1 == lado2 and lado2 == lado3:
    print('Esse triangulo é EQUILÁTERO!')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Esse triangulo é ISÓSCELES!')
else:
    print('Esse triangulo é ESCALENO')
        