print('\033[1;36m======= SUPERMERCADOS =======\033[m')
print('\033[1;33m-=\033[m' * 14)
print('\033[1;32mSELECIONE FORMA DE PAGAMENTO\033[m'.strip())
print('\033[1;33m-=\033[m' * 14)
print('A vista no DINHEIRO/CHEQUE: \033[;32m[1]\033[m')
print('A vista no CARTÃO: \033[;32m[2]\033[m')
print('Em até 2x no CARTÃO: \033[;32m[3]\033[m')
print('Em até 3x ou mais no CARTÃO: \033[;32m[4]\033[m')
preçonormal = float(input('Qual é o valor do produto? R$'))
formadepagamento = int(input('Qual forma de pagamento? '))
a = preçonormal - (preçonormal * 10 / 100)
b = preçonormal - (preçonormal * 5 / 100)
c = preçonormal
d = preçonormal + (preçonormal * 20 / 100)
if formadepagamento == 1:
    desconto = preçonormal * 10 / 100
    print('A forma de pagamento selecionado foi à vista no DINHEIRO/CHEQUE \ne seu desconto é de R${:.2f} e o valor total a ser pago ficou: \033[1;32mR${:.2f}\33[m'.format(desconto, a))
elif formadepagamento == 2:
    desconto = preçonormal * 5 / 100
    print('A forma de pagamento selecionado foi à vista no CARTÃO \ne seu desconto é de R${:.2f} e o valor total a ser pago ficou: \033[1;32mR${:.2f}\033[m'.format(desconto, b))
elif formadepagamento == 3:
    normal = preçonormal / 2
    print('A forma de pagamento selecionado foi em até 2x no CARTÃO \nde R${:.2f} e o valor total a ser pago ficou: \033[1;32mR${:.2f}\033[m'.format(normal, c))
elif formadepagamento == 4:
    parcelas = int(input('Quantas parcelas: '))
    juros = d / parcelas
    print('A forma de pagamento selecionado foi no CARTÃO \nem {}x de \033[31mR${:.2f}\033[m de juros e o valor total a ser pago ficou: \033[1;32mR${:.2f}\033[m'.format(parcelas, juros, d))
