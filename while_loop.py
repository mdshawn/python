# command =""

# while command.lower() != "exit":
#     command= input(">")
#     print("Echo" , command)



command = ""

while True:
    command = input(">")
    print("Echo",command)
    if command.lower() == "exit":
        break