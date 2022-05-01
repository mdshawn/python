# Python program to find largest
# number in a list
list1 = [10,20,50,80,100,200,300,400,500,600,700,800,900,1000]

max = list1[0]
for x in list1:
		if x > max :
			max = x

print(max)
