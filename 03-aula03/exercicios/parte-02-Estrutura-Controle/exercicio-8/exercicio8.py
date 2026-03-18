preco = 100
print("Se você comprar mais de 10 unidades, você ganha 10% de desconto no valor final")
produto = int(input("Quantos produtos você deseja comprar? "))
total = preco * produto

if produto >= 10:
    desconto = total * 0.10
    total = total - desconto

print("O valor total do produto é, ", total)