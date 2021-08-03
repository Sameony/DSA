#isBadVersion returns bool value whether that version is true or not
#latest version is bad version, its based on prev versions...find first bad
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return n
        left,right=1,n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left