l = float(input('Qual é a largura da parede?: '))
a = float(input('Qual é a altura da parede?: '))
A = l*a
q = (l*a)/2
print('A área dessa parede vale {:.3F} e precisará de {:.4f} litros de tinta para pinta-la: '.format(A,q))