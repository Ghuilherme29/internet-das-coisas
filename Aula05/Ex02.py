import os
os.system("cls")

Lista = []

while True:
    numero = int(input("Digite o number: "))

    if (numero!=0):
        Lista.append(numero)
    else:
        break
soma = sum()
print(f"Soma: {Lista}")
    
