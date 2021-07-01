#string to integer on leetcode
class Solution:
    def myAtoi(self, s: str) -> int:
        flag=0
        num=0
        s=s.lstrip()
        if not s:
            return 0
        if s[0]=='-':
            flag=1 
            s=s[1::]
        elif s[0]=='+':
            s=s[1::]
        for i in s:
            if not i.isdigit():
                break
            else:
                pnum=num*10 + int(i)
                if pnum>2147483647:
                    if flag==0:
                        num=2147483647
                    else:
                        num=-2147483648
                    return num
                else:
                    num=pnum
        if flag==0:
            return num
        return -num
            