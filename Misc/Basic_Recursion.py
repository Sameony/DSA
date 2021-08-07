#Sum Of 1_to_n
def SumToN(n:int):
    if n==0:
        return 0
    else:
        x= SumToN(n-1)
        s=n+x
        return s

print(SumToN(4))
