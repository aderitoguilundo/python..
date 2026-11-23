n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a outra nota: "))

md = (n1 + n2) / 2

if md < 5.0:
    print("Reprovado com media {:.2f}!".format(md))
elif md < 7:
    print("Estas em recuperacao com media {:.2f}!".format(md))
else:
    print("Estas aprovado com media {:.2f}!".format(md))