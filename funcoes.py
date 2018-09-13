def primo(num):
	count = 0
	for i in range(1, num + 1):
		if (num % i == 0):
			count+= 1
	if count == 2:
		return('SIM')
	else:
		return('NÃO')

def divisores(num):
	for i in range(1, num + 1):
		if (num % i == 0):
			print(f'{num} / {i} = {num / i:.0f}')

