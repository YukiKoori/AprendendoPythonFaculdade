v1 = float(input('digite o primeiro número'))
v2 = float(input('digite o segundo número'))

print('1-adição')
print('2-subtração')
print('3-multiplicação')
print('4-divisão')
opr = int(input('qual operação realizar digite'))

if(opr == 1):
    print(v1 + v2)
elif(opr == 2):
    print(v1 - v2)
elif(opr == 3):
    print(v1 * v2)
elif(opr == 4):
    print(v1 % v2)
