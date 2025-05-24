lado1 = float(input('insira o tamanho do primeiro lado:  '))
lado2 = float(input('insira o tamanho do segundo lado:  '))
lado3 = float(input('insira o tamanho do terceiro lado:  '))

if(lado1 > 0 and lado2 > 0 and lado3 > 0 and lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
 if(lado1 == lado2 == lado3):
    print('equilatero!')
 else:
    if(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
     print('escaleno!')
    else:
     print('isoseles!')
else:
  print('valor invalido')


#if( (norte or sul or oeste or leste) == True):
#print('você conseguiu escapar!')