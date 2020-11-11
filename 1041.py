# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

x,y = [float(x) for x in input().split()]

if (x == 0):
    if (y == 0):
        print('Origem')
    else:
        print('Eixo Y')
elif (x > 0):
    if (y == 0):
        print('Eixo X')
    elif(y > 0):
        print('Q1')
    elif(y < 0):
        print('Q4')
elif (x < 0):
    if (y == 0):
        print('Eixo X')
    elif(y > 0):
        print('Q2')
    elif(y < 0):
        print('Q3')