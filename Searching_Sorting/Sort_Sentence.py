#Sorting a shuffled sentence with position written at end of each word

def sortSentence(self, s: str) -> str:
    li=""
    x= s.split()
    li2=[None]*len(x)
    for i in x:
        n=int(i[-1])-1
        li2[n]=i[0:-1]
    c=1
    for i in li2:
        li+=i
        if c<len(x):
            li+= " "
        c+=1
    return li