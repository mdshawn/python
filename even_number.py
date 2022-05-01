count =0
for i in range(1 , 101):
    
    if i % 2 == 0:
        count+= 1
        print(f"{i} is a even number") 
print(f"We have found {count} even number")


for i in range(2 , 100 , 2):
    print(f"{i} is a even number")