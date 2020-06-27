from datetime import date

anoDeNascimento = int(input('Qual o ano que você nasceu? '))

idade = date.today().year - anoDeNascimento
if idade < 18:
    print('Você ainda vai se alistar.')
elif idade == 18:
    print('Você deve se alistar esse ano.')
else:
    print('Você passou {} anos do seu ano de alistamento'.format(idade - 18))