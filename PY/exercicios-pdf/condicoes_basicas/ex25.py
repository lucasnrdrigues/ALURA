s1 = float(input('Digite o valor do primeiro seguimento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('FORMA  um triângulo!')
else:
    print('NÃO FORMA um triângulo!')
