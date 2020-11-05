valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for cedula in cedulas:
    quantidade = (valor // cedula)
    valor -= (quantidade * cedula)
    print('{} nota(s) de R$ {},00'.format(quantidade, cedula))