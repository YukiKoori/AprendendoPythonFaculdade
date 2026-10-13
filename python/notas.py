nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))

media=(nota1*0.2+nota2*0.3+nota3*0.3)
print(f'a média geral é {media:.1f}')

if media>=70:
    print("Aprovado")
elif media>=50 and media<70:
    print("Recuperação")
else:    
    print("Reprovado")
