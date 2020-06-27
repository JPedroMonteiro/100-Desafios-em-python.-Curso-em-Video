valorDoProduto = float(input('Insira o valor do produto: '))
print('Digite a opção correspondente ao Modo de pagamento: ')
print('1 - A vista')
print('2 - cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
pagamento = int(input())

if pagamento == 1:
    print('Preço a pagar é de {}'.format(valorDoProduto - valorDoProduto*10/100))
elif pagamento == 2:
    novo = valorDoProduto - valorDoProduto*5/100
    print('Preço a pagar é de 2x de {:.2f}'.format(novo/2))
elif pagamento == 3:
    print('Preço a pagar é de 2x de {:.2f}'.format(valorDoProduto/2))
else:
    parcelas = int(input('Qual a quantidade de parcelas?'))
    valorComJuros = valorDoProduto*20/100 + valorDoProduto
    print('Preço a pagar é de {}x de {:.2f}'.format(parcelas, valorComJuros/parcelas))