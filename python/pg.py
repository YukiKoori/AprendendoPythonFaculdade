#coment{preco = float(input('insira o preço:'))
#desconto = float(input('percentual de desconto:' ))
#valor = preco*(desconto/100)
#resultado = preco - valor
#print(f'o preço é {preco} desconto de {desconto}%')
#print(f'o preço do produto é:{resultado}')

km = int(input('quantos km foram percorridos'))
dia = int(input('quantos dias foram usados'))

preco = (60 * dia) + (0.15 * km)

print(f'km {km}". dia {dia}')
print(f'o valor a ser pago é: {preco}')