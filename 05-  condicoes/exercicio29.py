v = float(input("Qual é a velocidade do carro?: "))
n = v*7
if(v > 80):
    print("Tens multa por andar a velociade de",v,"km/h")
    print("Tens de pagar",n,"Mt da multa")
else:
    print("Parabens, estás sem multa.")