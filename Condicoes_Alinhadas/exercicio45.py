from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("Suas opcoes:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")

jogador = int(input("Escolha uma opcao: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=-" * 11)
print("O computador escolheu: {}".format(itens[computador]))
print("O jogador escolheu: {}".format(itens[jogador]))
print("-=-" * 11)

if computador == jogador:
    print("Empate")
elif computador == 0:  # Computador Pedra
    if jogador == 1:
        print("Jogador venceu")
    else:
        print("Computador venceu")
elif computador == 1:  # Computador Papel
    if jogador == 2:
        print("Jogador venceu")
    else:
        print("Computador venceu")
elif computador == 2:  # Computador Tesoura
    if jogador == 0:
        print("Jogador venceu")
    else:
        print("Computador venceu")
else:
    print("Opcao invalida")