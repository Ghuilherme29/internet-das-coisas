import os
os.system("cls")

ListaInt = []

for i in range(6):
    numero = int(input("Digite um número: "))
    ListaInt.append(numero)
    
maior = max(ListaInt)
menor =  min (ListaInt) 
ListaInt.sort()

print(f"Maior number: {maior}")
print(f"Menor number: {menor}")
print(f"Ordem crescente: {sorted(ListaInt)}")

  