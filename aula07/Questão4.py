import os
os.system("cls")

try:

    nt1 = float(input("Digite a 1ª nota: "))
    nt2 = float(input("Digite a 2ª nota: "))
    nt3 = float(input("Digite a 3ª nota: "))

    media = (nt1 + nt2 + nt3) / 3

    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")


    print(f"Resultado da média: {media:.2f}")

except ValueError:
    print("Erro: Digite apenas números válidos.")