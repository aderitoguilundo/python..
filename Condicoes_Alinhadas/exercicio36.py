print("-=-" * 18)
print("Ola, aprovamos emprestimo para aquisicao de um bem")
print("-=-" * 18)

c = float(input("Qual e o valor da casa?: "))
s = float(input("Qual e o seu salario?: "))
a = int(input("Em quantos anos vai pagar? "))

p = c / (a * 12)
print("A prestacao e de {:.2f}".format(p))

m = s * (30 / 100)
if p <= m:
    print("O seu emprestimo aceite")
else:
    print("O seu emprestimo foi recusado")