print('escolha a fruta que deseja comprar: ')
print('1-maçã')
print('2-banana')
print('3-laranja')

produto = int(input('qual o produto 1, 2 ou 3: '))
quant = int(input('quantas: '))

if(produto == 1):
    pagar= quant*3.6
    print(f'você escolheu {quant} maçãs. O preço é: {pagar}')
else:
    if(produto == 2):
        pagar = quant* 1.85
        print(f'você escolheu {quant} bananas. O preço é: {pagar}')
    else:
     if(produto == 3):
         pagar = quant*2.31
         print(f'você escolheu {quant} laranjas. O preço é: {pagar}')
