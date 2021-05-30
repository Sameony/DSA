#Left shift multiplies by power of 2
#Right shift divides by power of 2
a=10
def deciToBin(a:int)->None:
    b=""
    while(a):
        b+=str(a&1)
        a=a>>1
    print("".join(b[::-1]))
deciToBin(10)