#Desafio: Verificar se o ano é bissexto.
#Minha solução------------------------------------------------------>
ano = int(input('Digite o ano: '))
if (ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0:
    print('O ano {} É bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))

#Guanabara----------------------------------------------->
#from datetime import date
#ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
#if ano == 0:
#    ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('O ano {} é BISSEXTO'.format(ano))
#else:
#    print('O ano {} NÃO é BISSEXTO'.format(ano))
