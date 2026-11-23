print("{:=^35}".format(" Loja Guilundo "))

p = float(input("Preco das compras: "))
print("Formas de pagamento:")
print("[1] a vista dinheiro / cheque")
print("[2] a vista a cartao")
print("[3] 2x a cartao")
print("[4] 3x ou mais no cartao...")

f = int(input("Digite a forma de pagamento: "))

if f == 1:
    t = p - (p * 10 / 100)
elif f == 2:
    t = p - (p * 5 / 100)
elif f == 3:
    t = p
    parcela = t / 2
    print("Sua compra sera parcelada em 2x de {:.2f}".format(parcela))
elif f == 4:
    t = p + (p * 20 / 100)
    parcelatotal = int(input("Quantas parcelas? "))
    parcelas = t / parcelatotal
    print("Sua compra sera parcelada em {}x de {:.2f} com juros".format(parcelatotal, parcelas))
else:
    t = p
    print("Opcao invalida, tente novamente")

print("Sua compra de {:.2f} vai custar {:.2f} no final.".format(p, t))