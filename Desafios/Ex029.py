#Desafio: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
#Minha Solução------------------------------------------------------>
velocidade = float(input('Digite a velocidade: '))
if velocidade > 80:
    print('Seu veiculo foi multado!')
    print('Valor da multa {}'.format((velocidade - 80.0)*7.0))

#Guanabara----------------------------------------------->
#velocidade = float(input('Qual é a velocidade atual do carro? '))
#if velocidade > 80:
#    print('Multado! Você excedeu o limitepermitido que é de 80Km/h')
#    multa = (velocidade - 80)*7.0
#    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
#print('Tenha um bom dia! Dirija com segurança!')
