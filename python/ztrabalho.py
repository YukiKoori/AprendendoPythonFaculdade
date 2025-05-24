#Escritas de boas vindas a loja:

print('Seja muito bem vindo a loja de Nayani Yara')
print('Adquirindo nossos produtos atinginto uma determinada meta, você poderá obter descontos na compra!')
print('Para prosseguir e descobrir o valor com desconto, preencha os tópicos a seguir:')


#valores utilizado para incrementar o desconto da loja.

val = float(input('Insira o valor do produto aqui:  '))
quant = int(input('Insira aqui a quantiade qual deseja comprar:  '))
res = val*quant


#resultados com if, elif, else com calculo incluso

if(res < 2500):
    print('Não foi dessa vez, você obteve 0% de desconto')
    print(f'Seu pedido sem desconto sairá por: RS{res}')
else:
    if(res >= 2500 and res < 6000):
     cal = res * 4 / 100
     prom = res - cal
     print('Você recebeu um desconto de 4% ')
     print(f'O valor total de seu pedido é: RS{res}')
     print(f'O valor total com desconto é: RS{prom}')
    elif(res >= 6000 and res < 10000):
     cal = res * 7 / 100
     prom = res - cal
     print('Você recebeu um desconto de 7% ')
     print(f'O valor total de seu pedido é: RS{res}')
     print(f'O valor total com desconto é: RS{prom}')
    elif(res >= 10000):
     cal = res * 11 / 100
     prom = res - cal
     print('Você recebeu um desconto de 11% ')
     print(f'O valor total de seu pedido é: RS{res}')
     print(f'O valor total com desconto é: RS{prom}')
    
    
#print finalização

print('Obrigado por adquirir os produtos da loja, volte sempre!')




