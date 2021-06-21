def LinSearch(nums:list[int], target:int):
    flag=0
    for i in range(len(nums)):
        if nums[i]==target:
            print(target," found at index: ",i)
            flag=1
            break
    if flag==0:
        print(target," Not found in array.")

n=int(input("Enter size of array: "))
print("Enter array: ")
li= [int(x) for x in input().split()]
tar=int(input("Enter number to be searched: "))
LinSearch(li,tar)