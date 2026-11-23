p = float(input("Digite o peso: "))
h = float(input("Qual e a sua altura? "))
imc = p / (h ** 2)

print("O IMC dessa pessoa e {:.2f}".format(imc))

if imc < 18.5:
    print("Voce esta abaixo do peso")
elif imc <= 25:
    print("Voce esta no peso ideal")
elif imc <= 30:
    print("Voce esta sobre peso")
elif imc <= 40:
    print("Voce esta sobre obesidade")
else:
    print("Cuidado, voce esta com obesidade morbida")