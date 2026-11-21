print("-"*15)
s = float(input("Qual é o seu salario? : "))

if s > 1250:
    a = s * (10 / 100)
    print("O seu aumento é {:.2f}".format(a))
else:
    a = s * (15 / 100)
    print("O seu aumento é {:.2f}!".format(a))
