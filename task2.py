n = int(input('Введите число '))
list_f = []
f = 1
for i in range(1, n + 1):
    f *= i
    print(f, end = ' ')
print()