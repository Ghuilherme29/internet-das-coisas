import os
os.system("cls")

while True:
    try:
        numeros = int(input("Digite o número:"))   
        
        for i in range(1,11):
            print(numeros, "x",i,"=", numeros*i)
        break 
    except: 
        print("Erro! Digite apenas números")  