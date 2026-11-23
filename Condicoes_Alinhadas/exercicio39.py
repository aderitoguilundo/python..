from datetime import date

atual = date.today().year
nasc = int(input("Digite o ano de nascimento: "))
idade = atual - nasc

print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))

if idade == 18:
    print("Voce tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento".format(saldo))
    print("O seu alistamento sera em {}".format(atual + saldo))
else:
    saldo = idade - 18
    print("Voce ja deveria ter se alistado ha {} anos".format(saldo))
    print("O seu alistamento foi em {}".format(atual - saldo))