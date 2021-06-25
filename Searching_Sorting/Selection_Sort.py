def SelecSort(arr:list[int])->list[int]:
    l=len(arr)
    for i in range (0,l-1):
        minInd=i
        for j in range(i+1,l):
            if arr[minInd]<arr[j]:
                minInd=j
        arr[i],arr[minInd]=arr[minInd],arr[i]
    return arr
x=[4,1,5,7,2,8,9,2,0]
x=SelecSort(x)
print(x)
x.reverse()
print(x)