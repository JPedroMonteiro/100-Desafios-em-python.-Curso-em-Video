a = int(input('Digite o primerio valor: '))
b = int(input('Digite o segundo Valor: '))

if a > b:
    print('{} é maior que {}'.format(a,b))
elif a < b:
    print('{} é maior que {}'.format(b,a))
else:
    print('{} e {} são iguais'.format(a,b))

