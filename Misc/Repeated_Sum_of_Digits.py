#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addDigits(self, num: int) -> int:
    if num%10==num:
        return num
        
    x=0
    while True:
        while(num):
            x+=num%10
            num=num//10
        if x%10==x:
            return x
        else:
            num=x
            x=0