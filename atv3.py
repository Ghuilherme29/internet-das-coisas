import os
os.system("cls")

temperatura = float(input("Digite a temperatura:"))

if temperatura <= 15:
    print (f"A temperatura é: {temperatura} - Frio")
elif temperatura >=15 and temperatura <= 25:
    print (f"A temperatura é {temperatura} - Está agradavel")
else:
    print(f"A temperatura é {temperatura} - Quente")     