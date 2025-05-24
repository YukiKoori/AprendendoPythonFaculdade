nota = 0
cont = 1

while (cont <= 3):
    x = float(input('digite sua nota aqui'))
    nota = nota + x
    cont = cont + 1
media = nota / 5
print(f'media final: {media}')

