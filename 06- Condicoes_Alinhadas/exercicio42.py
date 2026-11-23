print("-=-" * 12)
print("Analisando formacao de triangulo")
print("-=-" * 12)

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Com esses comprimentos pode se formar um triangulo! ", end="")
    if r1 == r2 == r3:
        print("Equilatero")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("Escaleno!")
    else:
        print("Isoceles!")
else:
    print("Nao tem como formar um triangulo com esses comprimentos")