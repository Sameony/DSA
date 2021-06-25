def bubbleSort(arr:list[int])->list[int]:
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr

potato=[1,2,3,6,2,9,2,97,12,-4]
potato=bubbleSort(potato)
print([potato])