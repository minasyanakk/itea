number = input("Введите число: ")

print("Вы ввели целое чилсло:{}\n Вещественное: {}\n Логическое:{}\n Строка: '{}'".format(int(number),float(number),bool(number),str(number)))


number2 = input("Введите второе число: ")

print("Целое + Вещественное ",int(number)+float(number2))
print("Строка + Строка ", str(number)+str(number2))
print("Целое * Вещественное ", int(number)*float(number2))

