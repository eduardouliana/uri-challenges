# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

lista = []
lista = ([int(x) for x in input().split()])

lista_ordenada = ([int(x) for x in lista])

lista_ordenada.sort()
for x in lista_ordenada:
    print(x)

print()

for x in lista:
    print(x)