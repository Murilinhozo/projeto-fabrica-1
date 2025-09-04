nota1 = float(input("Digite uma nota"))
nota2 = float(input("Digite outra nota"))
nota3 = float(input("Digite mais uma nota"))
nota4 = float(input("Digite a ultima nota"))
media = (nota1 + nota2 + nota3 + nota4)/4
print(media)

if media > 7.0:
    print(f"media: {media} - situação: aprovado")
elif media > 5.0 < 7.0:
    print(f"media: {media} - situação: recuperação")
else: 
    print(f"media: {media} - situação:reprovado")

