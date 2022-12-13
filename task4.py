n = int(input('Введите число N: '))
list_n = []
for i in range(-abs(n),abs(n) + 1):
    list_n.append(i)
print(list_n)
result = 1
path = 'file.txt'
with open(path, 'r') as data:
    for line in data:
        result *= list_n[int(line)] 
print(result)