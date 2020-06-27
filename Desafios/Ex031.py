#Desafio: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
#Minha solução------------------------------------------------------>
dist = float(input('Digite a distância em Km: '))
if dist <= 200:
    valor = dist*0.50
else:
    valor = dist*0.45
print('Valor da viagem: {:.2f}'.format(valor))

#Guanabara----------------------------------------------->
#distância = float(input('Qual é a distância da sua viagem? '))
#print('Você está prestes a começar uma viagem de {}Km'.format(distância))
#preço = distância*0.50 if distância <= 200 else distância*0.45
#print('E o preço de sua passagem será de R${:.2f}'.format(preço))
 