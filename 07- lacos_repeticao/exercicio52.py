n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('É por isso ele é primo')
else:
    print('É por isso ele não é primo')