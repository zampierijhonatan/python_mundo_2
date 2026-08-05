##Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa a ser comprada: '))
salario = float(input("Qual o seu salário atual: "))
anos = int(input('Em quantos anos pretende pagar a casa: '))

parcela = valor_casa / (anos * 12)
porcento = (salario * 30) / 100

if parcela > porcento:
    print('Sinto muito, o valor de {:.2f} excede seu limite aprovado!'.format(parcela))
else:
    print('Parabens! o valor de {:.2f} foi aprovado!'.format(parcela))

