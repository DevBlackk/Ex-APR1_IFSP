#print("Informa nome e notas do aluno a baixo.")
#nome = input("Nome: ")
#nota1 = float(input('Nota 1: '))
#nota2 = float(input('Nta 2: '))
#nota3 = float(input('Nota 3: '))

#media = (nota1 + nota2 + nota3) / 3

#print("A média de ", nome, "é: ", round(media, 2))

print("Informa nome e notas do aluno a baixo.")
nome = input("Nome: ")
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nta 2: '))

media = (nota1 + nota2) / 2

print("A média de ", nome, "é: ", round(media, 2))

if media >= 6:
  print("Você foi aprovado")
elif media >= 4:
  print("Em recperação")
else:
  print("Você foi reprovado")



