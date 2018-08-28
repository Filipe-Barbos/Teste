# Rodar script online
# https://trinket.io/features/python3

a =  int(input('Digite um número qualquer: '))
p = int(input('Digite um número primo: '))
result = 0
if (a % p) == 0:
	print('Primeira Fórmula')
	result = ((a**p) - a) / p
	if (((a**p) - a) % p) == 0:
		print(result)
		print('a e p são congruentes')
	else:
		print(result)
		print('a e p não são congruentes')

else:
	print('Segunda Fórmula')
	p2 = p -1
	result = (((a**p2)-1) / p)
	if (((a**p2)-1) % p) == 0:
		print(result)
		print('a e p são congruentes')
	else:
		print(result)
		print('a e p não são congruentes')

