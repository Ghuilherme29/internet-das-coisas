import os
os.system("cls")



try:
    idade = int(input("Digite a sua idade: "))
    if (idade>=18):
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")    
except:
    print("Dados Inválido! Digite somente números. ")