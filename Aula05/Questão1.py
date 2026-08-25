import os
os.system("cls")


negativos = []
positivo = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    
    if (num >= 0):
        positivo.append(num)
    else:
        negativos.append(num)
        

print("\n--- Resultados ---")
print(f"Quantidade de positivos: {len(negativos)}")
print(f"Quantidade de negativos: {len(positivo)}")
print(f"Vetor com os números negativos: {negativos}")
print(f"Soma dos números positivos: {sum(positivo)}")