print('-#-'*20)
print('Conversor de sistemas númericos!')
print('-#-'*20)
inteiro = int(input('Digite o número inteiro em Decimal: '))
print('\nQual será a base de conversão? ')
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
base = int(input())
print('Valor em decimal: {}'.format(inteiro))
if base == 1:
    novo = bin(inteiro)
    print('Valor em Binário: {}'.format(novo))
elif base == 2:
    novo = oct(inteiro)
    print('Valor em Octal: {}'.format(novo))
else:
    novo = hex(inteiro)
    print('Valor em Hexadecimal: {}'.format(novo))