# Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        else:
            res=[0,0]
            left,right=0,len(nums)-1
            while left<right:
                mid=(left+right)//2
                if target>nums[mid]:
                    left=mid+1
                else:
                    right=mid
            res[0]=left if nums[left]==target else -1
            left,right=0,len(nums)-1
            while left<right:
                mid=(left+right)//2+1
                if target<nums[mid]:
                    right=mid-1
                else:
                    left=mid
            res[1]=left if nums[left]==target else -1
        return res