def kmaxmin(nums:list[int], k:int):
    nums.sort(reverse=True)
    l=len(nums)
    print("Kth largest element = ",nums[k-1])
    print("Kth smallest element = ",nums[l-k-1])