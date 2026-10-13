R = float(input('Renda mensal'))
F = float(input('Finaciamentos:'))
if R>8500 and F<= 0.2*R:
    print('aprovado')
else:    
    print('negado')