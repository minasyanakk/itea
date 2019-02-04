#немного упростил 
num =  str(input("введите число: "))
num_2 = str(input("введите второе число: "))
x = ["-","+","*","**","/","%"]
for a in x:
	res=eval(num+a+num_2)
	print(num,a,num_2,"=",res)

