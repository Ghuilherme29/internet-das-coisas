carrinho = []

while True:
    produto = float(input("Digite o valor do produto: "))
    if (produto ==0):
        break
    else:
        carrinho.append(produto)
        
        
total = sum(carrinho)
print(f"o valor total da compra é : R$ {total:.2f}")        