# Rodar script online
# https://trinket.io/features/python3


a = int(input('Digite um número qualquer: '))
result = 0

# Verificando se p é primo
while True:
	p = int(input('Digite um número primo: '))
	cont = 0
	for i in range(1, p + 1):
		if p % i == 0:
			cont += 1
	
	if cont == 2:
		break
	else:
		print('{} não é primo!'.format(p))

if (a % p) == 0:
	result = ((a**p) - a) / p
	print("Primeira Fórmula")
	if (((a**p) - a) % p) == 0:
		print('Resultado: {}'.format(result))
		print('a e p são congruentes')
	else:
		print('Resultado: {}'.format(result))
		print('a e p não são congruentes')

else:
	p2 = p -1
	result = (((a**p2)-1) / p)
	print('Segunda Formula')
	if (((a**p2)-1) % p) == 0:
		print('Resultado: {}'.format(result))
		print('a e p são congruentes')
	else:
		print('Resultado: {}'.format(result))
		print('a e p não são congruentes')

