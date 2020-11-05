segundos = int(input())

MINUTOEMSEGUNDOS = 60
HORAEMSEGUNDOS = MINUTOEMSEGUNDOS * MINUTOEMSEGUNDOS

horas = (segundos // HORAEMSEGUNDOS)
segundos -= (horas * HORAEMSEGUNDOS)

minutos = (segundos // MINUTOEMSEGUNDOS)
segundos -= (minutos * MINUTOEMSEGUNDOS)

print('{}:{}:{}'.format(horas, minutos, segundos))