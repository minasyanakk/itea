first = input("Напишите ваше имя: ")
last = input("Напишите вашу фамилию: ")
print("Здравствуйте, {} {}".format(last,first))


day =int(input("Напишите день вашего роджения: "))
month = int(input("Напишите месяц вашего рождения: "))
year = int(input("Напишите год ващего рождения: "))

day_now= 31
month_now= 1
year_now = 2019

age = year_now - year

month_old = age *12 +month

day_old = month_old*30+day

print("Вам {0}, Вы прожили {1} месяцев и {2} Дней".format(age,month_old,day_old))