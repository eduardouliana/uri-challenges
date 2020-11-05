valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quantidade = (valor // nota)
    valor -= round((quantidade * nota), 2)
    print('{} nota(s) de R$ {:.2f}'.format(int(quantidade), nota))

print('MOEDAS:')
for moeda in moedas:
    # precisava disso, senão dava sempre erroooooo
    valor = round(valor, 2)
    quantidade = int(valor / moeda)
    valor -= (quantidade * moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(int(quantidade), moeda))    