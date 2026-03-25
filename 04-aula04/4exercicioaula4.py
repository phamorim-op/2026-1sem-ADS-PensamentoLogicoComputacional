idade = int(input("Qual é sua idade: "))

if idade >= 18 and idade < 60:
    print("Você é maior de idade!")
elif idade >= 60:
    print("Você é idoso(a)!")
else:
    print("Você é menor de idade!")