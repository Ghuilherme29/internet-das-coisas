import os
os.system("cls")
import random

numero = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero:
        print("Parabéns! Você acertou!")
        print("Tentativas:", tentativas)
        break

    elif palpite > numero:
        print("Seu palpite é maior que o número sorteado.")

    else:
        print("Seu palpite é menor que o número sorteado.")