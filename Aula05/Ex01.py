import os
os.system("cls")

temperatura = []

for x in range(5):
    temp = float(input(f"Digite a {x + 1}º temperatura: "))
    temperatura.append(temp)
 

media = sum(temperatura) / len(temperatura)
menor = min(temperatura)
maior = max(temperatura)

print(f"A maior temperatura: {maior} °C")    
print(f"A menor temperatura: {menor} °C")    
print(f"A média da temperatura: {media:.1f} °C")    