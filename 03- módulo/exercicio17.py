import math 
c1 = float(input("Digite o comprimento do cateto oposto: "))
c2 = float(input("Digite o comprimento do cateto adjacente: "))
hip = math.hypot(c1, c2)
print("O valor da hipotenusa é",hip)