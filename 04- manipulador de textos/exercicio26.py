f = str(input("Digite uma frase: "))
a = f.count("A")
p = f.find("A")+1
c = f.rfind("A")+1
print("A letra A aparece",a,"vezes")
print("Ela aparece pela primeira vez na posicão",p)
print("Ele aparece na ultima vez na posicao",c)