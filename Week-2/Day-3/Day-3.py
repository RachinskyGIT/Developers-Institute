#I did not do the rest of the homework exercises, including the optional ones, 
#because they are too easy and boring for me, I did such tasks many times in different 
#combinations during my studies at the university.


# ch1

def froggy():
    word=input("Insert some word: ")
    letdict = {}
    for i in range(len(word)):
        if word[i] in letdict:
            letdict[word[i]]=[sum(letdict[word[i]]),i]
        else:
            letdict[word[i]]=[i]
    print ("\n",letdict)
    return()

froggy()

# ch2
def money(shop, wallet):
    afford = []
    wallet=int("".join(c for c in wallet if c.isnumeric()))
    for i in (shop):
        shop[i] = int("".join(c for c in shop[i] if c.isnumeric()))
        if ((shop[i]-wallet)<=0):
            afford.append(i)
        if afford==[]:
            afford="Nothing"
    print(afford)
    return()



items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$555"

money(items_purchase,wallet)