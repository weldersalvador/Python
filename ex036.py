c = float(input('Digite o valor da casa: '))
s = float(input('Digite o valor do seu salário: '))
a = float(input('Em quantos anos você vai pagar?: '))
p = c / (a * 12)
print('Para pagar uma casa de {}R$ em {} anos a prestação será de {:.2f}R$'.format(c,a,p))
if p > (s + (30 * s) / 100):
    print('EMPRÉSTIMO NEGADO')
else:
    print('Emprestimo concedido!')
    print('O valor da prestação mensal será de {:.2f}R$'.format(p))
