import os
os.system('cls')

idade = int(input('Digite sua idade:'))

if idade >= 0 and idade <=12:
    print(f"sua idade: {idade} - Criança")

elif idade >= 13 and idade <= 18:
    print (f"Sua idade: {idade} - Adolescente")

elif idade >= 18 and idade <= 59:
    print (f"Sua idade: {idade} - Adulto")
else:
    print (f"sua idade: {idade} - Idoso")    