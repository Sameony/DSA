#Tradition
def revarr(nums:list[int]):
    i,l1=0,len(nums)
    n=l1
    while( i < (l1>>1)):
        nums[i],nums[n-i]=nums[i],nums[n-i]
        i+=1
    return nums

#Python Special

def revarrp(nums:list[int]):
    return nums[::-1]
