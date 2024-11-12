s1 = float(input('Digite o valor do primeiro seguimento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('FORMA  um triângulo!')
    if s1 == s2 and s2 == s3:
        print('O triângulo é EQUILÁTERO!')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('O triângulo é ISÓSCELES!')
    else:
        print('O triângulo é ESCALENO!')
else:
    print('NÃO FORMA um triângulo!')