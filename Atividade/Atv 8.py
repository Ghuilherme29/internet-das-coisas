import os
os.system("cls")
notas = []

while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))

    if nota == -1:
        break

    notas.append(nota)

print("\n===== NOTAS CADASTRADAS =====")

for nota in notas:
    print(nota)

if len(notas) > 0:

    print("\nQuantidade de notas:", len(notas))
    print("Média:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))

    notas.sort(reverse=True)

    print("Notas em ordem decrescente:", notas)

else:
    print("Nenhuma nota foi cadastrada.")