def Insertion( arr: list[int]):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

x=[5,3,8,2,9]
Insertion(x)
print(x)