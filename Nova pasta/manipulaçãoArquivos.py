#principal

#def criadas
def valid(pergunta,min,max):
  x = int(input(pergunta))
  while((x < min) or (x > max)):
    x = int(input(pergunta))
  return x

def existeAqv(NDA):
   try:
      a = open(NDA, 'rt')
      a.close()
   except FileNotFoundError:
      return False
   else:
      return True

def criarA(NdA):
  try:
      a = open(NdA, 'wt+')
      a.close()
  except():
     print('algo deu errado.')
  else:
      print(f'o arquivo {NdA} foi criado com sucesso!')

def cadastro(nmaqv,nomejogo,nomevg):
   try:
      a = open(nmaqv, 'at')
   except:
      print('erro ao abrir arquivo')
   else:
      a.write(f'{nomejogo};{nomevg} n')
   finally:
      a.close()

def listaraqv(nmaqv):
   try:
      a = open(nmaqv, 'rt')
   except:
      print('erro ao ler arquivo')
   else:
      print(a.read())
   finally:
      a.close()

#variavel
aqv = 'novo.arquivo'

#funções
if(existeAqv(aqv)):
   print('arquivo local')
else:
   print('inexistente')
   criarA

while True:
    print('menu')
    print('1- novo intem')
    print('2- cadastros')
    print('3- sair')

    op = valid('escolha a opção', 1, 3)

    if op == 1: #item
       print('new item...' )
       nomeJogo = input(' digite o nome aqui   ')
       nomeVDG = input(' Nome do VDG  ')
       cadastro(aqv,nomeJogo,nomeVDG)
       print('concluido.')
 
    elif op == 2: #cadastro
       print('Listar...' )
       listaraqv(aqv)

    elif op == 3: #encerrar
       print("finalizando...")
       break