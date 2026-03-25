num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))
num4 = int(input("Digite outro numero: "))
num5 = int(input("Digite outro numero: "))

list = [num1, num2, num3, num4, num5]

if 25 in list:
    print(f"O numero 25 está na lista")
else:
    print("Nenhum desses numeros não está na lista")