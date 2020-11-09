codigo, quantidade = [int(x) for x in input().split()]

map_cardapio = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

valor = map_cardapio[codigo]
total = (valor * quantidade)

print('Total: R$ {:.2f}'.format(total))