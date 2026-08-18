import os
os.system("cls")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "+":
        print(f"O resultado da soma é: {n1 + n2}")
    case "-":
        print(f"O resultado da subtração é: {n1 - n2}")
    case "*":
        print(f"O resultado da multiplicação é: {n1 * n2}")
    case "/":
        print(f"O resultado da divisão é: {n1 / n2}")