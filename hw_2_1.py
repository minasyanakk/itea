print("########################################")
num_1 = int(input("Введите первое число: >>>"))
num_2 = int(input("Введите второе число : >>>"))
print("########################################")
res=0

if num_1==num_2:
	print("Вы ввели одинаковые числа")


elif num_1<num_2:
	for x in range(num_1,num_2+1):
		res +=x
else:
	for x in range(num_2,num_1+1):
		res +=x

print(res)