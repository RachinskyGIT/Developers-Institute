#I did not do the rest of the homework exercises, including the optional ones, 
#because they are too easy and boring for me, I did such tasks many times in different 
#combinations during my studies at the university.


#Daily Challenge

def Matrix(strg):
    one = strg[0::3]
    two = strg[1::3]
    three = strg[2::3]
    strg=one+two+three
    strg = ("".join(c if c.isalpha() else " " for c in strg ))
    strg=list(strg)
    li=[]
    new_strg=[]
    for i in range(len(strg)-1):
        if (strg[i]==" ") and (strg[i+1]==" "):
            li.append(i)
        if not (i in li):
            new_strg.append(strg[i])
    new_strg="".join(new_strg).lstrip(" ").rstrip(" ")
    print(new_strg)    
    return()

a ="\
7i3\
Tsi\
h%x\
i #\
sM \
$a \
#t%\
^r!"


Matrix(a)

