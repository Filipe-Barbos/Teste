dados = list()
pessoas = list()

while True:
    dados.append(str(input('Nome:')).strip())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? (S/N): ')).strip().upper()
    while resp not in ('SN'):
        print('Resposta Inválida. Tente Novamente.')
        resp = str(input('Deseja continuar? (S/N): ')).strip().upper()
    
    if resp == 'N':
        break

print('=-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoa(s).')
print('-----PROGRAMA FINALIZADO COM SUCESSO-----')
