num = int(input("Введите число дня недели от 1 до 7: "))
if num < 1 or num > 7:
    print('Сказано же, от 1 до 7!')
elif num > 5:
    print('Ура.Выходной!')
else:
    print('Работай, скоро выходной!')