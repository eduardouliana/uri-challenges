dias = int(input())

MESESEMDIAS = 30
ANOSEMDIAS = 365

anos = (dias // ANOSEMDIAS)
dias -= (anos * ANOSEMDIAS)

meses = (dias // MESESEMDIAS)
dias -= (meses * MESESEMDIAS)

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))