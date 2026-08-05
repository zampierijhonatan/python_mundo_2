num = int(input('Digite um número para ser convertido: '))

print('''Escolha uma opção
[1] Decimal
[2]Hexadecimal
[3]Octal''')

opcao = int(input('Opção escolhida: '))

if opcao == 1:
    print('O número {} convertido em decimal é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido em hexadecimal é: {}'.format(num, hex(num)[2:]))
elif opcao == 3:
    print('O número {} convertido em octal é: {}'.format(num, oct(num)[2:]))
else:
    print('Digite uma opcao valida')