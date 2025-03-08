nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Agora digite a segunda nota:"))

media = (nota1+nota2)/2

print(f"A média do aluno é de: {media}")

if media >= 6:
    print("O aluno está aprovado.")
elif media >= 4:
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")