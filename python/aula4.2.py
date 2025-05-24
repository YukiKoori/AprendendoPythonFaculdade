x = 0
y = 0

for i in (0,101):
    if (i % 2 == 0):
        x += i
        y += i
media = x % y
print(f'a media de pares de 0 1 100 é: {media}')