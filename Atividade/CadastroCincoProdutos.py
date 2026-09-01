import os
os.system("cls")

listaProduto = []

for i in range(5):
    produto = (input("Adicione produtos: "))
    os.system("cls")
    listaProduto.append(produto)
    
totalProdutos = len(listaProduto)   

print(f"Lista de produtos: {listaProduto}")
print(f"Você adicionou um total de {totalProdutos} produtos.")    
