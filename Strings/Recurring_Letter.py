def Count_Letter(st1:str, target:chr)->int:
    st1=st1.lower()
    c=0
    for i in st1:
        if i==target:
            c+=1
    return c

x="Lgbtqrstuvwxyzoklahomapancakesorsomethingidontknow"
print(Count_Letter(x,'l'))
