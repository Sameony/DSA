#My naive solution
def plusOne(self, digits: List[int]) -> List[int]:
    if digits[-1] !=9:
        digits[-1]=digits[-1]+1
        return digits
    else:
        flag=0
        for i in digits:
            if i!=9:
                flag=1
                break
        if flag==0:
            digits.append(9)
            digits[0]=0
        x=[]
        c=1
        for i in reversed(digits):
            if i==9 and c==1:
                x.append(0)
            elif i!=9 and c==1:
                x.append(i+1)
                c=0
            else:
                x.append(i)
        return(reversed(x))

#Recursion with no extra space solution

def plusOne(self, digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = self.plusOne(digits[0:-1])
        return digits