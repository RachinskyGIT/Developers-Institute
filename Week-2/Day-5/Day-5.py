import os
import time
def clearscr():
    os.system('cls')


# fielddict = {1:".",2:".",3:".",4:".",5:".",6:".",7:".",8:".",9:"."}



# # def wh(): 
# #     choice = input("Choice area: ")
# #     return(choice)
# choice = 5
# choice = int(choice)

# turn=False  #True="X", False="O"



# while choice in range(1,10):
#     if turn==True:
#         fielddict[choice]="X"
#     else:
#         fielddict[choice]="O"
#     break

# n1,n2,n3,n4,n5,n6,n7,n8,n9 = [list(fielddict.items())[0][1],list(fielddict.items())[1][1]\
#                               ,list(fielddict.items())[2][1],list(fielddict.items())[3][1]\
#                                 ,list(fielddict.items())[4][1],list(fielddict.items())[5][1]\
#                                     ,list(fielddict.items())[6][1],list(fielddict.items())[7][1]\
#                                         ,list(fielddict.items())[8][1]]





# print(line)

def game(turn, gamedict):
    os.system('cls')
    gameend=False
    if gamedict=="start":
        turn=True #"X" starts
        fielddict = {"1":".","2":".","3":".","4":".","5":".","6":".","7":".","8":".","9":"."}
    else:
        fielddict=gamedict

    n1,n2,n3,n4,n5,n6,n7,n8,n9 = [list(fielddict.items())[0][1],list(fielddict.items())[1][1]\
                              ,list(fielddict.items())[2][1],list(fielddict.items())[3][1]\
                                ,list(fielddict.items())[4][1],list(fielddict.items())[5][1]\
                                    ,list(fielddict.items())[6][1],list(fielddict.items())[7][1]\
                                        ,list(fielddict.items())[8][1]]
    
    line = f"\
    \u269E \u2655 \u2655  \u2655 \u2654 \u2655 \u2655 \u2655 \u269F\n\
    |1    |2    |3    |\n\
    |  {n1}  |  {n2}  |  {n3}  |\n\
    |_____|_____|_____|\n\
    |4    |5    |6    |\n\
    |  {n4}  |  {n5}  |  {n6}  |\n\
    |_____|_____|_____|\n\
    |7    |8    |9    |\n\
    |  {n7}  |  {n8}  |  {n9}  |\n\
    |_____|_____|_____|\n"

    print(line)
    if turn==True:
        print('Player "X" turn\n')
    else:
        print('Player "O" turn\n')



    if (n1==n2==n3!=".") or (n4==n5==n6!=".") or (n7==n8==n9!=".") or\
       (n1==n4==n7!=".") or (n2==n5==n8!=".") or (n3==n6==n9!=".") or\
       (n1==n5==n9!=".") or (n3==n5==n7!="."):
        gameend=True

    if gameend==True:
        print("The Game is End")
        time.sleep(0.5)
        if turn==True:
            print('The "O"\u2015player is a winner! Congratulations!')
        else:
            print('The "X"\u2015player is a winner! Congratulations!')
        time.sleep(1.5)
        quit()



    goodchoice = ["1","2","3","4","5","6","7","8","9"]
    flag=True
    while flag==True:
        choice = input("Choice area: ")
        if choice == "stop":
            print("You choosed to end the game.\nGame will close in 5 seconds.")
            time.sleep(5)
            quit()
        if not choice in goodchoice:
            print("Please, insert number between 1 and 9")
            continue
        if (fielddict[choice]=="X") or (fielddict[choice]=="O"):
            print("This area is already taken. Please choose another area :)")
            continue           
        if choice in goodchoice:
            flag=False
            if turn==True:
                fielddict[choice]="X"
            else:
                fielddict[choice]="O"
            turn = not turn
            break
    game(turn, fielddict)
    
        
game(0,"start")





