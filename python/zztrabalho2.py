#inicio

print('Bem vindo a loja de gelados de Nayani Yara, prontos para anotar seus pedidos!')
print('---------------------Cardápio----------------------')
print('|','Tamanho', '|','Cupuaçu (CP)','|', 'Açaí(AC)','|')
print('|','   P   ', '|','  RS  9.00  ','|', 'RS 11,00','|')
print('|','   M   ', '|','  RS 14.00  ','|', 'RS 16,00','|')
print('|','   G   ', '|','  RS 18.00  ','|', 'RS 20,00','|')
print()

#loop

sabor = input('Qual sabor gostaria? Digite aqui CP ou AC:  ')
valor = 0

while(sabor == False or (sabor != 'CP' and sabor != 'AC')):
 print('sabor inválido, tente novamente...')
 sabor = input('Qual sabor gostaria CP ou AC?:  ')
if(sabor == 'CP'):
  valor += 9.00
  print('Você escolheu CP, vamos prosseguir...')
elif(sabor == 'AC'):
  valor += 11.00
  print('Você escolheu AC, vamos prosseguir...')


tam = input('Digite aqui P, M ou G:  ')

while(tam == False or (tam != 'P' and tam != 'M' and tam != 'G')):
 print('sabor inválido, tente novamente...')
 tam = input('Digite aqui P, M ou G:  ')

if(tam == 'P' and sabor == 'AC'):
  valor += 0
  print(f'Pequeno selecionado o valor é: {valor}')
elif(tam == 'M' and sabor == 'AC'):
  valor += 5.00
  print(f'Médio selecionado o valor é: {valor}')
elif(tam == 'G' and sabor == 'AC'):
  valor += 9.00
  print(f'Grande selecionado o valor é: {valor}')


elif(tam == 'P' and sabor == 'CP'):
  valor += 0
  print(f'Pequeno selecionado o valor é: {valor}')
elif(tam == 'M' and sabor == 'CP'):
  valor += 5.00
  print(f'Médio selecionado o valor é: {valor}')
elif(tam == 'G' and sabor == 'CP'):
  valor += 9.00
  print(f'Grande selecionado o valor é: {valor}')


