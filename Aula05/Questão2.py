import random

nomes = []

for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

sorteado = random.choice(nomes)

print(f"\nO nome sorteado foi: {sorteado}")