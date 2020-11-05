a, b, c = [float(x) for x in input().split()]

msg = 'Impossivel calcular'

delta = ((b ** 2) -4 * a * c)

if (delta < 0):
    print(msg)
    exit()

# elevando um número na potência 0.5, é o mesmo que fazer a raiz quadrada
raiz = (delta ** (1/2))
divisao = (2 * a)

if (divisao <= 0):
    print(msg)
    exit()
    
x1 = ((-b + raiz) / divisao)
x2 = ((-b -raiz) / divisao)

print('R1 = {:.5f}'.format(x1))
print('R2 = {:.5f}'.format(x2))