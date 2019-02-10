num_1 = 0
num_2 = 1
num_3 = int(input("Введите число: >>> "))
while True:
	print(num_1,end=" ")
	num_1, num_2 = num_2, num_1 + num_2
	if num_1>=num_3:
		break