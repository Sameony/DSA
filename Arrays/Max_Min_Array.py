def MaxMin(nums:list[int]):
    print("Maximum value: ", max(nums))
    print("Minimum value: ",min(nums))

#Tradition

def MaxMinArray(nums:list[int]):
    i=nums[0]
    m1,m2=i,i
    for i in nums:
        if i<m1:
            m1=i
        if i>m2:
            m2=i
    print("Maximum value: ", m1)
    print("Minimum value: ",m2)