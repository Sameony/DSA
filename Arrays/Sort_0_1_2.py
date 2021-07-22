#Sorting an array consisting of only 0s and 1s without using sorting algo
def mySort( arr:list[int])->list[int]:
    l=len(arr)
    c0=0
    for i in range(l):
        if arr[i]==0:
            arr[i],arr[c0]=arr[c0],arr[i]
            c0+=1
        
    for i in range(l):
        if arr[i]==1:
            arr[i],arr[c0]=arr[c0],arr[i]
            c0+=1
    return arr

x=[2,2,1,0,1,2,0,0,1]
print(x)
x=mySort(x)
print(x)