import os
def clearscr():
    os.system('cls')

line0  = "    ___________________0\n"
line1  = "    |1    |2    |3    |1\n"
line2p = "    |  .  |  .  |  .  |2\n"   # 7 / 13 / 19 - indexes of dots
line3  = "    |_____|_____|_____|3\n"
line4  = "    |4    |5    |6    |4\n"
line5p = "    |     |     |     |5\n"
line6  = "    |_____|_____|_____|6\n"
line7  = "    |7    |8    |9    |7\n"
line8p = "    |     |     |     |8\n"
line9  = "    |_____|_____|_____|9\n"

line2p = list(line2p)




fieldlist = [[None,None,None],[None,None,None],[None,None,None]]
# fieldlist = [[1,2,3],[4,5,6],[7,8,9]]
sublist = []
fielddict = {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
fielddict2 = {line2p[7]:None, line2p[13]:None, line2p[19]:None,4:None,5:None,6:None,7:None,8:None,9:None}
# def wh(): 
#     choice = input("Choice area: ")
#     return(choice)
choice = 5
# fieldlist[choice]=True


strg = "    |_____|_____|_____|9\n"
strg = list(strg)
strg[13]="X"
strg = "".join(strg)
print(strg)


# for i in range(len(fielddict2)):
#     list(fielddict2.items())[0][0] = "X"
    
print(type(line2p))








# for 
#     line2p[7] = 
#     line2p[13]=
#     line2p[19]=
#     line5p[7] =
#     line5p[13]=
#     line5p[19]=
#     line8p[7] =
#     line8p[13]= 
#     line8p[19]=











# if choice in range(1,4):
#     line_selector = choice-1
#     sublist=fieldlist[0] #line2p   # 7 / 13 / 19 - indexes of dots
#     sublist[line_selector] = True
#     fieldlist[0] = sublist
#     fielddict[choice-1]=True

# elif choice in range(4,7):
#     line_selector = choice-4
#     sublist=fieldlist[1] #line5p
#     sublist[line_selector] = True
#     fieldlist[1] = sublist
#     fielddict[choice-1]=True

# elif choice in range(7,10):
#     line_selector = choice-7
#     sublist=fieldlist[2] #line8p
#     sublist[line_selector] = True
#     fieldlist[2] = sublist
#     fielddict[choice-1]=True

# print(fielddict)








