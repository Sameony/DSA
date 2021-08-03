#x^4=(x*x)^2
#x^5=x*(x*x)^2

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n==0:
            return 1
        elif x==0:
            if n<0:
                return float('inf')
            else:
                return 0
        elif n<0:
            x=1/x
            n=-n
        def potat(x,n):
            if n==1:
                return x
            else:
                if n%2==1:
                    return x*self.myPow(x*x,(n-1)//2)
                else:
                    return self.myPow(x*x,n//2)
        return potat(x,n)
        