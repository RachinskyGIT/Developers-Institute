goodchoice = ["1","2","3","4","5","6","7","8","9"]
flag=True
while flag==True:
    # if not (str(choice).isdecimal and (int(choice) in range(1,10))): 
    choice = input("Choice area: ")
    if not choice in goodchoice:
        print("Please, insert number between 1 and 9")
        continue
    while int(choice) in range(1,10):
        flag=False
        print ("Yes")
        break

print("End")
