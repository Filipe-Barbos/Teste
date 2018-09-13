import Funcoes

n1 = int(input('Digite um número: '))

result = n1 * n1 - n1 + 41

print(f'Resultado da equação: {result}')

num_primo = Funcoes.primo(result)
print(f'{result} é um número primo: {num_primo}')

Funcoes.divisores(result)
