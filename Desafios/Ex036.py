print('-:-'*20)
print('Validação de Empréstimo Bancário')
print('-:-'*20)
valorCasa = float(input('Qual é o valor da casa? R$'))
valorDoSalario = float(input('Qual é o valor do salário? R$'))
anos = float(input('Em quantos anos se dará o pagamento? '))
parcela = valorCasa/(12*anos)
limite = valorDoSalario*30/100

if parcela > limite:
    print('A parcela de R${} excede o limite de 30% do salario que é igual a R${}'.format(parcela, limite))
else:
    print('Parcela R${}. Limite R${}. Meses {}. Emprestimo Aprovado!'.format(parcela, limite, anos*12))
