import os
os.system("cls")

nomes = []

for i in range(5):
    nome = input("Insira os nomes: ")
    nomes.append(nome)

nomes.sort()
print("Nomes em ordem alfabética: ")
for nome in nomes:
    print(f"- {nome}")




