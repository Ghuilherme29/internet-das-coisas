import random, os, time

numero_secreto = random.randint(1,100)
tentativas = 0

while True:
    try:
        numero = int(input("Chute um númerode 1 a 100: "))
        tentativas += 1
        
        if numero > numero_secreto:
            print("O número secreto é menor. Tente novamente!\n")
            time.sleep(1)
            os.system("cls")
        elif numero < numero_secreto:
            print("O número secreto é maior. Tente novamente!\n") 
            time.sleep(1)
            os.system("cls")
        else:
            print ("Parabéns, Você acertou!")
            print(f"Você acertou em {tentativas} tentativas.")
            break
    except ValueError:
        print("Digite somente números inteiros.")