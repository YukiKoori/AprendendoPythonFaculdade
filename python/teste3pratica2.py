#preço a pagar pelofornecimento de enegia eletrica

print('bem vindos a central de pagamento, respontas as seguintes perguntas para prosseguir com o pagamento:  ')
cons = float(input('quantos kwh foram consumidos nesta semana:  '))

print('R = Residência')
print('C = Comércio')
print('I = Indústria')
res = input('qual sua residencia:  ')

if(res == 'R'):
    if(cons >= 500):
     preco = 0.65
    else: (cons < 500)
    preco = 0.55
    valor = cons * preco
    print(f'O valor total è {valor} obrigado por ultilizar nossos seviços!')
elif(res == 'C'):
    if(cons >= 1000):
       preco = 0.80
    else:(cons < 1000)
    preco = 0.75
    valor = cons * preco
    print(f'O valor total è {valor} obrigado por ultilizar nossos seviços!')
elif(res == 'I'):
    if(cons >= 1500):
     preco = 0.90
    else:(cons < 1500)
    preco = 0.85
    valor = cons * preco
    print(f'O valor total è {valor} obrigado por ultilizar nossos seviços!')
 