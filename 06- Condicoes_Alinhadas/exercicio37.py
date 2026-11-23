n = int(input("Digite um numero inteiro: "))

print("Escolha uma das bases de conversao:")
print("[1] para binario")
print("[2] para octal")
print("[3] para hexadecimal")

opcao = int(input("Sua escolha: "))

if opcao == 1:
    print("{} para Binario e igual a {}".format(n, bin(n)[2:]))
elif opcao == 2:
    print("{} para Octal e igual a {}".format(n, oct(n)[2:]))
elif opcao == 3:
    print("{} para Hexadecimal e igual a {}".format(n, hex(n)[2:]))
else:
    print("Opcao invalida.")