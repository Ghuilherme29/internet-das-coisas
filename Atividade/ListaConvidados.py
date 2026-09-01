import os
os.system("cls")

ListaNomes = []

while True:
    nomes = input("Digite os nomes: ")
    
    
    if (nomes != "fim"):
        ListaNomes.append(nomes)
    else:
        break

TotalConvidados = len(ListaNomes)
ListaNomes.sort()

print(f"Nomes inseridos: {ListaNomes}")
print(f"Quantidade de nomes inseridos: {len(ListaNomes)}")
print(f"Ordem Alfabetica de nomes: {sorted(ListaNomes)}")
 