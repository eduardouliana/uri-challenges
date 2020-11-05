a, b, c, d = [int(x) for x in input().split()]

msg = 'Valores nao aceitos'
try:
    if (b <= c):
        exit()
    if(d <= a):
        exit()
    if((c + d) <= (a + b)):
        exit()
    if(c < 0):
        exit()
    if(d < 0):
        exit()
    if(a % 2 != 0):
        exit()
        
    msg = 'Valores aceitos'
finally:
    print(msg)